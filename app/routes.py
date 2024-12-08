import sys
from fastapi import Request, FastAPI, APIRouter
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from app.services.form_validation_service import FormValidationService
from app.repositories.form_validation_repository import FormValidationRepository
from app.config import config

router = APIRouter()
form_repo = None
form_service = None

try:

    c = MongoClient(config['MONGO_CONNECTION_URL'])
    db = c[config['MONGO_DB']]
    db.command('ping')
    col = db[config['MONGO_COLLECTION']]

    form_repo = FormValidationRepository(col)
    form_service = FormValidationService(form_repo)
except Exception as e:
    raise RuntimeError(f'MongoDB connection failed: {e}')

@router.post('/get_form')
async def get_form(request: Request):
    body = await request.json()
    types = form_service.get_types(body)
    form_name = form_service.get_form_name(types)
    if form_name is None:
        return JSONResponse(types)
    return JSONResponse({
       'form_name': form_name
    })
