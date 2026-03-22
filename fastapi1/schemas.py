from pydantic import BaseModel
class ItemBase(BaseModel):
    nome: str | None = None
    preco: float | None = None 
    em_oferta: bool | None = False 
class ItemRequisicao(ItemBase):
    ... 
class ItemResposta(ItemBase):
    id: int
    class Config:
        from_attributes = True
 