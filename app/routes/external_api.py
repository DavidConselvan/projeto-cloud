from fastapi import FastAPI, Depends, APIRouter, HTTPException, Query
from app.database import SessionDep
from app.utils import verify_credentials
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

router = APIRouter()

import requests

app = FastAPI()

@router.get("/consultar/", summary = "Consultar infos de Mercado", description = "Consultar principais infos diárias de Mercado")
def get_stocks_prices(
    token: str = Depends(verify_credentials)  # Validate JWT token before proceeding
):
    if not RAPIDAPI_KEY:
        raise HTTPException(status_code=500, detail="Chave API não configurada")

    url = "https://seeking-alpha.p.rapidapi.com/market/get-day-watch"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Erro ao buscar valores de mercado")
    
    return response.json()
