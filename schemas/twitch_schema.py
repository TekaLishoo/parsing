from typing import Optional
from pydantic import BaseModel, Field
from datetime import date, datetime


class StreamSchema(BaseModel):
    user_login: str
    game_name: str
    type: str
    title: str
    viewer_count: int
    language: str
    is_mature: bool
    create_date: date = Field(default_factory=datetime.today)


class UpdateStreamModel(BaseModel):
    user_login: Optional[str]
    game_name: Optional[str]
    type: Optional[str]
    title: Optional[str]
    viewer_count: Optional[int]
    language: Optional[str]
    is_mature: Optional[bool]
    create_date: Optional[date]
