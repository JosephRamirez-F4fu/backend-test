from typing import Union, Optional

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()
class Book(BaseModel):
    title: str
    Author: str
    year: int
    pages: Optional[int]

@app.post("/book")
async def addBook(book: Book):
    return {"book":book}

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/hello")
async def hello():
    return {"hello": "world"}