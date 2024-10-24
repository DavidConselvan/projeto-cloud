from typing import Optional
from sqlmodel import Field, SQLModel
from pydantic import EmailStr

class UserModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr = Field(index=True, unique=True, max_length=255)
    name: str
    password: str = Field(min_length=8, max_length=255)

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "joaosilva@gmail.com",
                "name": "João da Silva",
                "password": "12345678"
            }
        }
    }

class LoginModel(SQLModel):
    email: EmailStr = Field(max_length=255)
    password: str = Field(min_length=8, max_length=255)

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "joaosilva@gmail.com",
                "password": "12345678"
            }
        }
    }

class Token(SQLModel):
    jwt: str


    