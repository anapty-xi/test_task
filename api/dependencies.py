from infrastructure.dish_statistics import DishStatisticInfrastructure
from usecases.dish_statistics.usecases import Analyze


def analyze_usecase() -> Analyze:
    return Analyze(DishStatisticInfrastructure())
