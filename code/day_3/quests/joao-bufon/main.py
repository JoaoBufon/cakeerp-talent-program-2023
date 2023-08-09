from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

@app.get("/status/")
def read_status():
    return{"status": "it's alive"}

