from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routes import user, login, external_api

app = FastAPI()

#Ensure that the database and tables are created when the application starts
@app.on_event("startup")
def startup_event():
    create_db_and_tables()
   
#Root route
@app.get("/")
def root():
    return {"message": "Bem vindo a API Restful de Cloud"}

#Include the routers
app.include_router(user.router)
app.include_router(login.router)
app.include_router(external_api.router)


