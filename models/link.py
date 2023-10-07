from sqlalchemy import Column, String
from models import base


class Link(base.BaseModel):
    __tablename__ = "links"

    address = Column(String)
    short = Column(String(8), index=True, unique=True)
