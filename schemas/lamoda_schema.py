from typing import Optional
from pydantic import BaseModel, Field
from datetime import date, datetime


class ProductSchema(BaseModel):
    category: str
    brand: str
    name: str
    price: float = Field(..., gt=0.0)
    description: Optional[dict]
    create_date: date = Field(default_factory=datetime.today)


class UpdateProductModel(BaseModel):
    category: Optional[str]
    brand: Optional[str]
    name: Optional[str]
    price: Optional[float]
    description: Optional[dict]
    create_date: Optional[date]
