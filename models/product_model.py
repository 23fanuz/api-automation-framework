from pydantic import BaseModel
from typing import Optional

class Rating(BaseModel):
    rate: float
    count: int

class Product(BaseModel):
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: Rating
