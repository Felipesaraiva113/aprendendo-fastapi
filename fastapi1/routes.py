from fastapi import APIRouter 
from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session 
from database import get_db 
from repositories import ItemRepository 
from schemas import ItemRequisicao, ItemResposta 
from models import Item
items_router = APIRouter(tags=['itens'])
@items_router.get('/itens/{id}', response_model = ItemResposta)
async def encontrar_por_id(id: int, db: Session = Depends(get_db)):
    item = ItemRepository.encontrar_por_id(db, id)
    if not item:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND, detail = 'Item não encontrado'
        ) 
    return ItemResposta.model_validate(item)
@items_router.put('/itens/{id}', response_model= ItemResposta)
async def atualizar(id: int, requisicao: ItemRequisicao, db: Session = Depends(get_db)):
    item_db = ItemRepository.encontrar_por_id(db, id)
    if not item_db:
        raise HTTPException(status_code=404, detail='Item não encontrado!')
    item_atualizado = ItemRepository.atualizar(db, item_db, requisicao.model_dump(exclude_unset=True))
    return item_atualizado
@items_router.get('/itens/', response_model= list[ItemResposta])
async def obter_todos(db: Session = Depends(get_db)):
    itens = ItemRepository.encontrar_todos(db)
    return [ItemResposta.model_validate(item) for item in itens]
@items_router.delete('/itens/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def deletar_por_id(id: int, db: Session = Depends(get_db)):
    item_db = ItemRepository.encontrar_por_id(db, id)
    if not item_db:
        raise HTTPException(status_code=404, detail='Item não localizado')
    ItemRepository.deletar_por_id(db, id)
    print('--- item deletado com sucesso! ---')
    return Response(status_code=status.HTTP_204_NO_CONTENT)
@items_router.post('/itens/', response_model= ItemResposta, status_code=status.HTTP_201_CREATED)
async def criar(requisicao: ItemRequisicao, db: Session = Depends(get_db)):
    item = ItemRepository.criar_item(db, Item(**requisicao.model_dump(exclude_unset=True)))
    print('--- item adicionado com sucesso! ---')
    return ItemResposta.model_validate(item)
