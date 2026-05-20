from pydantic import BaseModel
from typing import List


class CartProduct(BaseModel):
    productId: int
    quantity: int


class Order(BaseModel):
    id: int
    userId: int
    date: str
    products: List[CartProduct]
