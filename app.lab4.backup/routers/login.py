import os
"""
This module provides routes for authentication.
"""

from app import templates
#from app import DEPLOY_REF
from app.utils.auth import AuthCookie, get_login_form_creds, get_auth_cookie
from app.utils.exceptions import UnauthorizedPageException

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from typing import Optional

router = APIRouter()


@router.get(
  path="/login",
  summary="Gets the login page",
  tags=["Pages", "Authentication"],
  response_class=HTMLResponse
)
async def get_login(
  request: Request,
  invalid: Optional[bool] = None,
  logged_out: Optional[bool] = None,
  unauthorized: Optional[bool] = None):

  context = {
    'request': request,
    'deploy_ref': os.environ.get('DEPLOY_REF', ''),
    'invalid': invalid,
    'logged_out': logged_out,
    'unauthorized': unauthorized
  }
  return templates.TemplateResponse("pages/login.html", context)


@router.post(
  path="/login",
  summary="Logs into the app",
  tags=["Authentication"]
)
async def post_login(cookie: Optional[AuthCookie] = Depends(get_login_form_creds), request: Request = None):
  if cookie:
    # Если клиент хочет JSON (например, API-тест), возвращаем JSON
    if request and "application/json" in request.headers.get("accept", ""):
      return JSONResponse({"status": "ok", "token": cookie.token})
    response = RedirectResponse('/reminders', status_code=302)
    response.set_cookie(key=cookie.name, value=cookie.token)
  else:
    if request and "application/json" in request.headers.get("accept", ""):
      return JSONResponse({"status": "error"}, status_code=401)
    response = RedirectResponse('/login?invalid=True', status_code=302)
  
  return response


logout = dict(
  path="/logout",
  summary="Logs out of the app",
  tags=["Authentication"]
)
@router.get(**logout)
@router.post(**logout)
async def logout_route(cookie: Optional[AuthCookie] = Depends(get_auth_cookie)) -> dict:
  if not cookie:
    raise UnauthorizedPageException()
  
  response = RedirectResponse('/login?logged_out=True', status_code=302)
  response.set_cookie(key=cookie.name, value=cookie.token, expires=-1)
  return response
