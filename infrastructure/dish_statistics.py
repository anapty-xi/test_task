from entities.base import CategoryStatistic, DishMargin


class DishStatisticInfrastructure:
    async def generate_suggestions(
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
