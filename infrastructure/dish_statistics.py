from collections import defaultdict

from entities.base import CategoryStatistic, DishMargin
from entities.dish_statistics import DishStatistics
from entities.report import Report


class DishStatisticInfrastructure:
    async def analyze(self, dishes_stats: list[DishStatistics]) -> Report:
        total_revenue = sum(d.revenue() for d in dishes_stats)
        total_margin = sum(d.margin() for d in dishes_stats)
        margin_percent = total_margin / total_revenue * 100 if total_revenue else 0

        dishes_stats = sorted(
            dishes_stats, key=lambda x: x.margin_percent(), reverse=True
        )

        top_margin_dishes, loss_making = self._top_loss_margin(dishes_stats)
        by_category = self._by_category(dishes_stats)

        suggestions = await self._generate_suggestions(
            top_margin_dishes, loss_making, by_category
        )

        return Report(
            total_revenue,
            total_margin,
            margin_percent,
            top_margin_dishes,
            loss_making,
            by_category,
            suggestions,
        )

    async def _generate_suggestions(
        self,
        top_margin: list[DishMargin],
        loss_making: list[DishMargin],
        by_category: dict[str, CategoryStatistic],
    ) -> list[str]:
        return [
            "Отличная маржа за сегодня",
            "Вы точно не отмываете деньги?",
            "Можешь похвастаться маме",
        ]

    def _top_loss_margin(
        self, dishes_stats: list[DishStatistics]
    ) -> tuple[list[DishMargin], list[DishMargin]]:
        top_margin_dishes = []
        loss_making = []

        for dish in dishes_stats:
            margin_entity = DishMargin(dish.dish_name, dish.margin_percent())
            if dish.margin_percent() >= 30:
                top_margin_dishes.append(margin_entity)
            else:
                loss_making.append(margin_entity)

        return top_margin_dishes, loss_making

    def _by_category(
        self,
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

            by_category[cat] = CategoryStatistic(revenue, margin, margin_percent)

        return by_category
