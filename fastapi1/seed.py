from database import SessionLocal 
from models import Item 
from repositories import ItemRepository 
db = SessionLocal()
item = Item(nome='Intel Core i7 3400', preco=500, em_oferta=True) 
ItemRepository.criar_item(db, item)
db.close()
print('Produto inserido com sucesso!')
