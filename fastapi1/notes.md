from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Item(BaseModel):
    nome: str
    preco: float 
    em_oferta: Union[bool, None] = None

@app.get('/itens/{item_id}')
async def ler_item(item_ud: int, q: Union[str, None] = None):
    return {'item_id': item_ud, 'q': q}
@app.put('/itens/{item_id}')
async def atualizar_item(item_id: int, item: Item):
    return {'nome_do_item': item.nome, 'item_id': item_id}