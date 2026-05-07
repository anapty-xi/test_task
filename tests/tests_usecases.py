from decimal import Decimal

import pytest

from entities.dish_statistics import DishStatistics
from usecases.dish_statistics.usecases import Analyze


async def test_total_revenue_and_margin(dishes, mock_inf):
    report = await Analyze(mock_inf).execute(dishes)

    assert report.total_revenue == Decimal("16520")
    assert report.total_margin == Decimal("10990")


@pytest.mark.asyncio
async def test_top_margin_dishes_sorted_descending(dishes, mock_inf):
    report = await Analyze(mock_inf).execute(dishes)

    percents = [d.margin_percent for d in report.top_margin_dishes]
    assert percents == sorted(percents, reverse=True)


@pytest.mark.asyncio
async def test_loss_making_below_threshold(mock_inf):
    low_margin_dish = DishStatistics(
        dish_id=1,
        dish_name="Стейк рибай",
        cost_price=Decimal("800.00"),
        selling_price=Decimal("950.00"),
        quantity=5,
        category="Мясо",
    )
    report = await Analyze(mock_inf).execute([low_margin_dish])

    assert len(report.loss_making) == 1
    assert report.loss_making[0].dish_name == "Стейк рибай"
    assert len(report.top_margin_dishes) == 0


@pytest.mark.asyncio
async def test_by_category_aggregation(dishes, mock_inf):
    report = await Analyze(mock_inf).execute(dishes)

    assert set(report.by_category.keys()) == {"Паста", "Салаты", "Пицца"}
    assert report.by_category["Пицца"].revenue == Decimal("8000")
    assert report.by_category["Пицца"].margin == Decimal("5750")
