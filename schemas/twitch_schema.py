from typing import Optional
from pydantic import BaseModel, Field
from datetime import date, datetime


class StreamSchema(BaseModel):
    description: list
    pagination: dict
    create_date: date = Field(default_factory=datetime.today)


class UpdateStreamModel(BaseModel):
    description: Optional[list]
    pagination: Optional[dict]
    create_date: Optional[date]
