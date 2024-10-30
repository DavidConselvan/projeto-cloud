from fastapi import APIRouter, HTTPException
from app.models import LoginModel, UserModel, Token
from app.database import SessionDep
from app.utils import auth_password, create_token
from sqlmodel import select

router = APIRouter()

#Routes
@router.post("/login/", summary = "Login", description = "Login de usuário", response_model = Token) 
def login(login: LoginModel, session: SessionDep):
    user = session.exec(select(UserModel).where(UserModel.email == login.email)).first()
    if user is None or not auth_password(login.password, user.password):
        raise HTTPException(status_code = 401, detail = "Email ou senha inválidos")
    
    return {"jwt": create_token(data={"sub": user.email})}