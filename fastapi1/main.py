# COMANDO DO UVICORN = uvicorn main:app --reload
from fastapi import FastAPI
from database import engine, Base 
from routes import items_router
Base.metadata.create_all(bind = engine)
app = FastAPI() 
app.include_router(items_router)
@app.get('/') 
async def read_root():
    return {'olá': 'mundo'} # mensagem temporária

