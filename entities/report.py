from decimal import Decimal

from pydantic import BaseModel

from entities.base import CategoryStatistic, DishMargin


class Report(BaseModel):
    total_revenue: Decimal
    total_margin: Decimal
    margin_percent: Decimal
    top_margin_dishes: list[DishMargin]
    loss_making: list[DishMargin]
    by_category: dict[str, CategoryStatistic]
    suggestions: list[str]
