from pydantic import BaseModel
from fastapi import HTTPException
from database.vendas import vendas
from login.login import userLogin as user

class Item(BaseModel):
    user: str
    password: str

class VendaCreate(BaseModel):
    item: str
    preco_unitario: float
    quantidade: int



def get_vendas(item: Item):
    if item.user == user["usuario"] and item.password == user["senha"]:
       return {"msg": "Acesso permitido",  "data": vendas}
    raise HTTPException(status_code=400, detail="Acesso negado!")

def insert_vendas(venda: VendaCreate):
    if venda.preco_unitario <= 0 or venda.quantidade <= 0 :
        raise HTTPException(status_code=400, detail="Campo(s) obrigatorio(s) vazio(s)")
    
    valor_total = venda.preco_unitario * venda.quantidade
    novo_id = max(vendas[-1].keys()) + 1

    nova_venda = {
        novo_id: {
            "item" : venda.item,
            "preco_unitario": venda.preco_unitario,
            "quantidade": venda.quantidade,
            "valor_total": valor_total
        }
    }

    vendas.append(nova_venda)
    return {"message": "Venda cadastrada com sucesso",  "valor_total": valor_total}

    
