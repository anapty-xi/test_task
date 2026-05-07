from decimal import Decimal


def test_revenue(dish):
    # 450 * 12 = 5400
    assert dish.revenue() == Decimal("5400")


def test_total_cost(dish):
    # 180 * 12 = 2160
    assert dish.total_cost() == Decimal("2160")


def test_margin(dish):
    # (450 - 180) * 12 = 3240
    assert dish.margin() == Decimal("3240")


def test_margin_percent(dish):
    # 3240 / 5400 * 100 = 60.00
    assert dish.margin_percent() == Decimal("60.00")
