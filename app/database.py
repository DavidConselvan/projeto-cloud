from sqlmodel import create_engine, Session, SQLModel
from fastapi import Depends
from dotenv import load_dotenv
from typing import Annotated
import os

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
        
SessionDep = Annotated[Session, Depends(get_session)]
    
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

