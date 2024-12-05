from fastapi import Request, FastAPI, APIRouter
from fastapi.responses import JSONResponse
from models import *

router = APIRouter()

@router.post('/get_form', response_model=GetFormResponse)
async def get_form(request: Request):
   body = await request.json()
   if False:
      return JSONResponse({
         'hey': 'a'
      })
   else:
      return GetFormResponse(name='a')
