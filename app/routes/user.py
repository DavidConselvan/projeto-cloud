from fastapi import APIRouter, HTTPException
from app.models import UserModel, Token
from app.database import SessionDep
from app.utils import hash_password, create_token
from sqlmodel import select

router = APIRouter()

@router.post("/registrar/", summary="Registrar", description="Fazer Cadastramento de usuário", response_model=Token)
def registrar(user: UserModel, session: SessionDep):
    user_db = session.exec(select(UserModel).where(UserModel.email == user.email)).first()
    if user_db:
        raise HTTPException(status_code=409, detail="Email já cadastrado")
    
    user.password = hash_password(user.password)
    session.add(user)
    session.commit()
    session.refresh(user)

    return {"jwt": create_token(data={"sub": user.email})}
