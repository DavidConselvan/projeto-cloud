from passlib.context import CryptContext
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import JWTError
from typing import Union
from dotenv import load_dotenv
import os

load_dotenv()

# Create a CryptContext for hashing passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to hash the password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Secret key for signing the JWT tokens (make sure this is kept secret)
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"  # Algorithm used to sign the JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time

oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "/login")

# Function to create a JWT token
def create_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def auth_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def auth_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="JWT ausente ou inválido",
        headers={"Authorization": "Bearer <JWT>"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        return {"email": email}
    except JWTError:
        raise credentials_exception