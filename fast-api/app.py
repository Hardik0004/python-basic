from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory "database" as a list for demonstration purposes
fake_db = []


class Item(BaseModel):
    name: str
    description: str


class ItemResponse(BaseModel):
    id: int
    name: str
    description: str


@app.post("/items/", response_model=ItemResponse, status_code=201)
def create_item(item: Item):
    item_id = len(fake_db)
    item_response = ItemResponse(id=item_id, **item.model_dump())
    fake_db.append(item_response)
    return item_response


@app.get("/items/", response_model=List[ItemResponse])
def read_items():
    return fake_db


@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]


@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, updated_item: Item):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")
    item_response = ItemResponse(id=item_id, **updated_item.model_dump())
    fake_db[item_id] = item_response
    return item_response


@app.delete("/items/{item_id}", response_model=ItemResponse)
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = fake_db.pop(item_id)
    return deleted_item
