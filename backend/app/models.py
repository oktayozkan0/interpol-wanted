from pydantic import BaseModel
from typing import Optional


class Criminal(BaseModel):
    forename: Optional[str] = None
    name: Optional[str] = None
    date_of_birth: Optional[str] = None
    entity_id: str
    thumbnail: Optional[str] = None
    url: Optional[str] = None
    date: str
