# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from typing import List
# from .database import get_collection

# router = APIRouter()

# class Item(BaseModel):
#     name: str
#     description: str
#     price: float

# @router.post("/items/", response_model=Item)
# async def create_item(item: Item):
#     collection = get_collection("items")
#     result = await collection.insert_one(item.dict())
#     if result.inserted_id:
#         return item
#     raise HTTPException(status_code=400, detail="Item could not be created")

# @router.get("/items/", response_model=List[Item])
# async def read_items():
#     collection = get_collection("items")
#     items = await collection.find().to_list(100)
#     return items

# @router.get("/items/{item_id}", response_model=Item)
# async def read_item(item_id: str):
#     collection = get_collection("items")
#     item = await collection.find_one({"_id": item_id})
#     if item:
#         return item
#     raise HTTPException(status_code=404, detail="Item not found")

# @router.delete("/items/{item_id}")
# async def delete_item(item_id: str):
#     collection = get_collection("items")
#     result = await collection.delete_one({"_id": item_id})
#     if result.deleted_count == 1:
#         return {"detail": "Item deleted"}
#     raise HTTPException(status_code=404, detail="Item not found")