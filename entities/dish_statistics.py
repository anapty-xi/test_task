from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, Field


class DishStatistics(BaseModel):
    dish_id: Annotated[int, Field(ge=1)]
    dish_name: str
    cost_price: Annotated[Decimal, Field(ge=0)]
    selling_price: Annotated[Decimal, Field(ge=0)]
    quantity: Annotated[int, Field(ge=0)]
    category: str

    def revenue(self) -> Decimal:
        return self.selling_price * self.quantity

    def total_cost(self) -> Decimal:
        return self.cost_price * self.quantity

    def margin(self) -> Decimal:
        return (self.selling_price - self.cost_price) * self.quantity

    def margin_percent(self) -> Decimal:
        return self.margin() / self.revenue() * 100
