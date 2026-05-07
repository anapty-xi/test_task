from datetime import date

from pydantic import BaseModel, ConfigDict

from entities.dish_statistics import DishStatistics
from entities.report import Report


class DishStatisticsInput(BaseModel):
    date: date
    sales: list[DishStatistics]


class ReportOut(Report):
    model_config = ConfigDict(from_attributes=True)
    pass
