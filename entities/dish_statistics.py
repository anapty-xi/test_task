from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class DishStatistics(BaseModel):
    """
    Raw sales and cost data for an individual dish entry.

    Contains pricing and quantity information, with built-in methods
    to calculate revenue, total cost, and margin at the unit level.
    """

    model_config = ConfigDict(from_attributes=True)

    dish_id: Annotated[int, Field(ge=1)]
    dish_name: str
    cost_price: Annotated[Decimal, Field(ge=0, decimal_places=2)]
    selling_price: Annotated[Decimal, Field(ge=0, decimal_places=2)]
    quantity: Annotated[int, Field(ge=0)]
    category: str

    def revenue(self) -> Decimal:
        return self.selling_price * self.quantity

    def total_cost(self) -> Decimal:
        return self.cost_price * self.quantity

    def margin(self) -> Decimal:
        return (self.selling_price - self.cost_price) * self.quantity

    def margin_percent(self) -> Decimal:
        return (self.margin() / self.revenue() * 100).quantize(Decimal("0.01"))
