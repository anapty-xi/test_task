from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, Field

from entities.base import CategoryStatistic, DishMargin


class Report(BaseModel):
    """
    Comprehensive analytical report for sales performance.

    Consolidates overall financial totals, categorized breakdowns,
    profitability rankings (top-margin vs. loss-making), and
    system-generated business recommendations.
    """

    total_revenue: Annotated[Decimal, Field(decimal_places=2)]
    total_margin: Annotated[Decimal, Field(decimal_places=2)]
    margin_percent: Annotated[Decimal, Field(decimal_places=2)]
    top_margin_dishes: list[DishMargin]
    loss_making: list[DishMargin]
    by_category: dict[str, CategoryStatistic]
    suggestions: list[str]
