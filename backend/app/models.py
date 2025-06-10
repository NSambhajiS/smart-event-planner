# from pydantic import BaseModel
# from typing import Optional, List

# class Item(BaseModel):
#     id: Optional[str] = None
#     name: str
#     description: Optional[str] = None
#     price: float
#     tags: List[str] = []

# class User(BaseModel):
#     id: Optional[str] = None
#     username: str
#     email: str
#     full_name: Optional[str] = None
#     disabled: Optional[bool] = None

# class Order(BaseModel):
#     id: Optional[str] = None
#     user_id: str
#     item_ids: List[str]
#     total_price: float
#     status: str