from typing import Annotated

from fastapi import APIRouter, Body, Depends

from api.dependencies import analyze_usecase
from api.serializers import DishStatisticsInput, ReportOut
from usecases.dish_statistics.usecases import Analyze

router = APIRouter(prefix="/analyze_sales", tags=["analyze"])


@router.post("/")
async def analyze_sales(
    dishes_stats: Annotated[DishStatisticsInput, Body()],
    usecase: Annotated[Analyze, Depends(analyze_usecase)],
) -> ReportOut:
    report = await usecase.execute(dishes_stats.sales)
    return ReportOut.model_validate(report)
