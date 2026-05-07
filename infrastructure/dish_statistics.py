from entities.base import CategoryStatistic, DishMargin


class DishStatisticInfrastructure:
    async def generate_suggestions(
        self,
        top_margin: list[DishMargin],
        loss_making: list[DishMargin],
        by_category: dict[str, CategoryStatistic],
    ) -> list[str]:
        """
        Generates a list of text recommendations based on analyzed sales data.

        :param top_margin: List of dishes with high profitability (>= 30%).
        :param loss_making: List of dishes with low or negative profitability.
        :param by_category: Dictionary of aggregated statistics
            grouped by category name.
        :return: A list of string suggestions for the business owner.
        """
        return [
            "Отличная маржа за сегодня",
            "Вы точно не отмываете деньги?",
            "Можешь похвастаться маме",
        ]
