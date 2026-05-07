from collections import defaultdict

from entities.base import CategoryStatistic, DishMargin
from entities.dish_statistics import DishStatistics
from entities.report import Report
from usecases.dish_statistics.protocol import DishStatisticProtocol


class Analyze:
    def __init__(self, inf: DishStatisticProtocol):
        self.inf = inf

    async def execute(self, dishes_stats: list[DishStatistics]) -> Report:
        total_revenue = sum(d.revenue() for d in dishes_stats)
        total_margin = sum(d.margin() for d in dishes_stats)
        margin_percent = total_margin / total_revenue * 100 if total_revenue else 0

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
        category_map = defaultdict(list)

        for dish in dishes_stats:
            category_map[dish.category].append(dish)

        by_category = {}
        for cat, dishes in category_map.items():
            revenue = sum(d.revenue() for d in dishes)
            margin = sum(d.margin() for d in dishes)
            margin_percent = margin / revenue * 100 if revenue else 0

            by_category[cat] = CategoryStatistic(
                revenue=revenue, margin=margin, margin_percent=margin_percent
            )

        return by_category
