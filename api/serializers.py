from datetime import date
from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class DishStatisticsDTO(BaseModel):
    dish_id: Annotated[
        int, Field(ge=1, description="Unique identifier for the dish", examples=[1])
    ]
    dish_name: str = Field(
        description="The name of the dish", examples=["Pasta Carbonara"]
    )
    cost_price: Annotated[
        Decimal,
        Field(
            ge=0,
            decimal_places=2,
            description="Production cost per unit",
            examples=["150.00"],
        ),
    ]
    selling_price: Annotated[
        Decimal,
        Field(
            ge=0,
            decimal_places=2,
            description="Retail price per unit",
            examples=["450.00"],
        ),
    ]
    quantity: Annotated[
        int, Field(ge=0, description="Number of units sold", examples=[10])
    ]
    category: str = Field(
        description="The category the dish belongs to", examples=["Main Course"]
    )


class DishStatisticsInput(BaseModel):
    date: date
    sales: list[DishStatisticsDTO]


class DishMarginDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    dish_name: str = Field(
        description="Official name of the dish from the menu", examples=["Cheeseburger"]
    )
    margin_percent: Annotated[
        Decimal,
        Field(
            decimal_places=2,
            description="Calculated profit margin percentage for this item",
            examples=["42.50"],
        ),
    ]


class CategoryStatisticDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    revenue: Annotated[
        Decimal,
        Field(
            decimal_places=2,
            description="Total sales income for this specific category",
            examples=["3200.00"],
        ),
    ]
    margin: Annotated[
        Decimal,
        Field(
            decimal_places=2,
            description="Net profit contribution from this category",
            examples=["960.00"],
        ),
    ]
    margin_percent: Annotated[
        Decimal,
        Field(
            decimal_places=2,
            description="Weighted average margin percentage for all items in this category",
            examples=["30.00"],
        ),
    ]


class ReportDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    total_revenue: Annotated[
        Decimal,
        Field(
            decimal_places=2, description="The sum of all sales", examples=["15250.75"]
        ),
    ]
    total_margin: Annotated[
        Decimal,
        Field(decimal_places=2, description="Total gross profit", examples=["4850.25"]),
    ]
    margin_percent: Annotated[
        Decimal,
        Field(
            decimal_places=2,
            description="Overall profitability ratio expressed as a percentage",
            examples=["31.80"],
        ),
    ]
    top_margin_dishes: list[DishMarginDTO] = Field(
        description="Collection of high-performance dishes meeting profitability targets"
    )
    loss_making: list[DishMarginDTO] = Field(
        description="Collection of dishes with margins below the acceptable threshold"
    )
    by_category: dict[str, CategoryStatisticDTO] = Field(
        description="Financial performance breakdown indexed by menu category name"
    )
    suggestions: list[str] = Field(
        description="Strategic business advice generated based on the report data",
        examples=[["Boost promotion for high-margin items"]],
    )
