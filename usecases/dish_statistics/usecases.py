from collections import defaultdict
from decimal import Decimal

from entities.base import CategoryStatistic, DishMargin
from entities.dish_statistics import DishStatistics
from entities.report import Report
from usecases.dish_statistics.protocol import DishStatisticProtocol


class Analyze:
    """
    Business logic interactor for analyzing sales performance.

    Coordinates the calculation of global financial metrics, categorizes items
    based on profitability thresholds, aggregates statistics by category,
    and fetches business recommendations via the infrastructure layer.
    """

    def __init__(self, inf: DishStatisticProtocol):
        self.inf = inf

    async def execute(self, dishes_stats: list[DishStatistics]) -> Report:
        """
        Orchestrates the full analysis process for a given list of sales data.

        :param dishes_stats: A list of dish-level sales statistics.
        :return: A comprehensive Report entity containing calculated insights.
        """
        total_revenue = sum((d.revenue() for d in dishes_stats), Decimal("0"))
        total_margin = sum((d.margin() for d in dishes_stats), Decimal("0"))
        margin_percent = (
            (total_margin / total_revenue * 100).quantize(Decimal("0.01"))
            if total_revenue
            else Decimal(0)
        )

        dishes_stats = sorted(
            dishes_stats, key=lambda x: x.margin_percent(), reverse=True
        )

        top_margin_dishes, loss_making = self._top_loss_margin(dishes_stats)
        by_category = self._by_category(dishes_stats)

        suggestions = await self.inf.generate_suggestions(
            top_margin_dishes, loss_making, by_category
        )

        return Report(
            total_revenue=total_revenue,
            total_margin=total_margin,
            margin_percent=margin_percent,
            top_margin_dishes=top_margin_dishes,
            loss_making=loss_making,
            by_category=by_category,
            suggestions=suggestions,
        )

    @staticmethod
    def _top_loss_margin(
        dishes_stats: list[DishStatistics],
    ) -> tuple[list[DishMargin], list[DishMargin]]:
        """
        Splits dishes into high-margin (top) and low-margin (loss-making) groups.
        A dish is categorized as 'top-margin' if its profitability is 30% or higher.

        :param dishes_stats: A list of dish-level sales statistics.
        :return: tuple contains top margin dishes[0] and loss making dishes[1]
        """
        top_margin_dishes = []
        loss_making = []

        for dish in dishes_stats:
            margin_entity = DishMargin(
                dish_name=dish.dish_name, margin_percent=dish.margin_percent()
            )
            if dish.margin_percent() >= 30:
                top_margin_dishes.append(margin_entity)
            else:
                loss_making.append(margin_entity)

        return top_margin_dishes, loss_making

    @staticmethod
    def _by_category(
        dishes_stats: list[DishStatistics],
    ) -> dict[str, CategoryStatistic]:
        """
        Groups sales data by category and calculates aggregate statistics for each.

        :param dishes_stats: A list of dish-level sales statistics.
        :return: Dict, keys - categories, values - category
        statistics(revenue, margin, margin percent)
        """
        category_map = defaultdict(list)

        for dish in dishes_stats:
            category_map[dish.category].append(dish)

        by_category = {}
        for cat, dishes in category_map.items():
            revenue = sum((d.revenue() for d in dishes), Decimal("0"))
            margin = sum((d.margin() for d in dishes), Decimal("0"))
            margin_percent = (
                (margin / revenue * 100).quantize(Decimal("0.01"))
                if revenue
                else Decimal(0)
            )

            by_category[cat] = CategoryStatistic(
                revenue=revenue, margin=margin, margin_percent=margin_percent
            )

        return by_category
