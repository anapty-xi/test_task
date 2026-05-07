from typing import Protocol

from entities.base import CategoryStatistic, DishMargin


class DishStatisticProtocol(Protocol):
    async def generate_suggestions(
        self,
        top_margin: list[DishMargin],
        loss_making: list[DishMargin],
        by_category: dict[str, CategoryStatistic],
    ) -> list[str]: ...
