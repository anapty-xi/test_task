from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, Field


class DishMargin(BaseModel):
    """
    Data model representing the profitability metric for a specific dish.
    Used to rank and identify high-performing or underperforming menu items.
    """

    dish_name: str
    margin_percent: Annotated[Decimal, Field(decimal_places=2)]


class CategoryStatistic(BaseModel):
    """
    Aggregate financial metrics for a specific menu category.
    Includes total revenue, total margin, and calculated average margin percentage.
    """

    revenue: Annotated[Decimal, Field(decimal_places=2)]
    margin: Annotated[Decimal, Field(decimal_places=2)]
    margin_percent: Annotated[Decimal, Field(decimal_places=2)]
