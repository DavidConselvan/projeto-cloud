from fastapi import FastAPI, Depends, APIRouter, HTTPException, Query
from app.database import SessionDep
from app.utils import auth_user

router = APIRouter()

import requests

app = FastAPI()

@router.get("/consultar/")
def get_market_quotes(ticker: str = Query(..., description= "Ticker de uma STOCK"), auth_user= Depends(auth_user)):
    url = "https://seeking-alpha.p.rapidapi.com/market/get-realtime-quotes"
    querystring = {"symbols": ticker}
    headers = {
        "X-RapidAPI-Key": "9dc0cd25c5msh7093cea7eab33dbp1ed6d1jsne0b3a44acc73",
        "X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Erro ao buscar valores de mercado")
    
    return response.json()
