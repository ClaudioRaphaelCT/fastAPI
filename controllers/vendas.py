from pydantic import BaseModel
from fastapi import HTTPException
from database.vendas import vendas

class Item(BaseModel):
    user: str

def get_vendas(item: Item):
    if item.user == "Raphael":
       return {"msg": "Acesso permitido",  "data": vendas}
    raise HTTPException(status_code=400, detail="Acesso negado!")
    
