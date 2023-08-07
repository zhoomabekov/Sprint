from typing import List

from fastapi import FastAPI, status, HTTPException

import models_sql
from database import SessionLocal
from models_py import Item

app = FastAPI()

db = SessionLocal()


@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get('/items', response_model=List[Item], status_code=200)
async def get_all_items():
    items = db.query(models_sql.Item).all()

    return items

@app.post('/items', response_model=Item,
          status_code=status.HTTP_201_CREATED)
async def create_an_item(item: Item):
    db_item = db.query(models_sql.Item).filter(models_sql.Item.name == item.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail="Item already exists")

    new_item = models_sql.Item(
        name=item.name,
        price=item.price,
        description=item.description,
        on_offer=item.on_offer
    )

    db.add(new_item)
    db.commit()

    return new_item

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

