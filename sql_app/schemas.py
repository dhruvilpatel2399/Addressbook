from typing import List, Optional
from unicodedata import name

from pydantic import BaseModel


class AddressBase(BaseModel):
    name:str
    address:str
    longitude:float
    latitude:float

    class Config:
        orm_mode = True




# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     items: List[Item] = []

#     class Config:
#         orm_mode = True
