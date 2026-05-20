from app import templates, DEPLOY_REF
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("pages/login.html", {"request": request, "DEPLOY_REF": DEPLOY_REF})

@router.get("/favicon.ico")
async def get_favicon():
    return FileResponse("static/img/favicon.ico")

@router.get("/not-found")
async def get_not_found(request: Request):
    return templates.TemplateResponse("pages/not-found.html", {'request': request})
