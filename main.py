from fastapi import FastAPI
from database.vendas import vendas
from controllers.vendas import Item, get_vendas

app = FastAPI()


@app.get('/')
def home():
    return 'Hello API'

@app.post('/vendas')
def obter_vendas(item: Item):
    return get_vendas(item)
