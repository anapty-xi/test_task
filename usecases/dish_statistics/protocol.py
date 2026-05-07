from typing import Protocol

from entities.dish_statistics import DishStatistics
from entities.report import Report


class DishStatisticProtocol(Protocol):
    async def analyze(self, dishes_stats: list[DishStatistics]) -> Report: ...
