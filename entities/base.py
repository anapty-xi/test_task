from decimal import Decimal

from pydantic import BaseModel


class DishMargin(BaseModel):
    dish_name: str
    margin_percent: Decimal


class CategoryStatistic(BaseModel):
    revenue: Decimal
    margin: Decimal
    margin_percent: Decimal
