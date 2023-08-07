from pydantic import BaseModel
from typing import Optional, List


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    price: int
    on_offer: Optional[bool] = False

    class Config:
        orm_mode = True
