from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return{"messege": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id : int):
    return{"item_id": item_id}


fake_customers_db =[{'item_name': 'Maria' },{'item_name': 'Nascimento'}, 
{'item_name': 'Raimundo' }, {'item_name': 'Assis' },{'item_name': 'Gerlane' }]

@app.get("/customers/")
def read_item(skip : int = 0, limit : int = 10):
    return fake_customers_db[skip:skip + limit]


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool,None] = None

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
