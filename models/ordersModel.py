from pydantic import BaseModel, Field
from models.criterionModel import CriterionModel

class OrdersModel(BaseModel):
    id: int = Field(gt=0, description="The price must be greater than zero")
    item: str = Field(title="Item name", max_length=300, min_length=1)
    quantity: int = Field(gt=0, description="The price must be greater than zero")
    price: float = Field(gt=0, description="The price must be greater than zero")
    status: CriterionModel