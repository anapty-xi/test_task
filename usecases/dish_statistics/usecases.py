from usecases.dish_statistics.protocol import DishStatisticProtocol


class Analyze:
    def __init__(self, inf: DishStatisticProtocol):
        self.inf = inf

    async def execute(self, dishes_stats):
        return await self.inf.analyze(dishes_stats)
