from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base 
class Item(Base):
    __tablename__ = 'itens'
    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome: str = Column(String(100), nullable= False)
    preco: float = Column(Float, nullable=False)
    em_oferta: bool = Column(Boolean, default=False)
    def __init__(self, nome, preco, em_oferta = False):
        self.nome = nome 
        self.preco = preco 
        self.em_oferta = em_oferta 
  