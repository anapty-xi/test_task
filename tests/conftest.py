from decimal import Decimal
from unittest.mock import AsyncMock

import pytest

from entities.dish_statistics import DishStatistics


@pytest.fixture
def dish() -> DishStatistics:
    return DishStatistics(
        dish_id=1,
        dish_name="Паста Карбонара",
        cost_price=Decimal("180.00"),
        selling_price=Decimal("450.00"),
        quantity=12,
        category="Паста",
    )


@pytest.fixture
def mock_inf():
    inf = AsyncMock()
    inf.generate_suggestions.return_value = ["suggestion"]
    return inf


@pytest.fixture
def dishes() -> list[DishStatistics]:
    return [
        DishStatistics(
            dish_id=1,
            dish_name="Паста Карбонара",
            cost_price=Decimal("180.00"),
            selling_price=Decimal("450.00"),
            quantity=12,
            category="Паста",
        ),
        DishStatistics(
            dish_id=2,
            dish_name="Цезарь с курицей",
            cost_price=Decimal("140.00"),
            selling_price=Decimal("390.00"),
            quantity=8,
            category="Салаты",
        ),
        DishStatistics(
            dish_id=3,
            dish_name="Маргарита",
            cost_price=Decimal("90.00"),
            selling_price=Decimal("320.00"),
            quantity=25,
            category="Пицца",
        ),
    ]
