from fastapi import FastAPI
from database.vendas import vendas # Dados do banco de dados , pasta DATABASE, vendas.py
from controllers.vendas import Item, VendaCreate, get_vendas, insert_vendas #Regra para acessar as rotas

app = FastAPI()


@app.get('/')
def home():
    return 'Simple API CRUD'

@app.post('/vendas')
def obter_vendas(item: Item):
    return get_vendas(item)

@app.post('/adicionar')
def adicionar(venda: VendaCreate):
    return insert_vendas(venda)
