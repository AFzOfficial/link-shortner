import pydantic
from datetime import datetime


class LinkInput(pydantic.BaseModel):
    address: str


class LinkOutput(pydantic.BaseModel):
    id: int
    address: str
    short: str
    created_at: datetime
    updated_at: datetime
