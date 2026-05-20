"""
This module provides routes for root and favicon.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

from app import templates
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse


# --------------------------------------------------------------------------------
# Router
# --------------------------------------------------------------------------------

router = APIRouter()


# --------------------------------------------------------------------------------
# Routes
# --------------------------------------------------------------------------------

@router.get(
    path="/",
    summary="Returns the login page (public)",
    tags=["Pages"]
)
async def read_root(request: Request):
    # Возвращаем страницу логина без редиректа, чтобы check мог прочитать deploy-ref
    return templates.TemplateResponse("pages/login.html", {"request": request})


@router.get(
    path="/favicon.ico",
    include_in_schema=False
)
async def get_favicon():
    return FileResponse("static/img/favicon.ico")


@router.get(
    path="/not-found",
    summary="Gets the \"Not Found\" page",
    tags=["Pages"]
)
async def get_not_found(request: Request):
    return templates.TemplateResponse("pages/not-found.html", {'request': request})
