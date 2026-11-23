from pydantic import BaseModel, Field
from decimal import Decimal

class ItemCreate(BaseModel):
    item_cost = Field(
        gt = 0,
        max_digits = 10,
        decimal_places=2
    )
    item_descripton = str = Field(
        min_length=3,
        max_length = 200
    )
    
class ItemUpdate(BaseModel):

    item_cost: Decimal | None = Field(
        default=None,
        gt=0,
        max_digits=10,
        decimal_places=2
    )

    item_description: str | None = Field(
        default=None,
        min_length=3,
        max_length=200
    )