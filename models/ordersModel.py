from pydantic import BaseModel, Field
from typing import Literal

class OrdersModel(BaseModel):
    id: int = Field(gt=0, description="The price must be greater than zero")
    item: str = Field(title="Item name", min_length=1)
    quantity: int = Field(gt=0, description="The price must be greater than zero")
    price: float = Field(gt=0, description="The price must be greater than zero")
    status: Literal["completed", "pending", "canceled", "all"]