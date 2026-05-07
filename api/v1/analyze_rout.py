from typing import Annotated

from fastapi import APIRouter, Body, Depends

from api.dependencies import analyze_usecase
from api.serializers import DishStatisticsInput, ReportDTO
from entities.dish_statistics import DishStatistics
from usecases.dish_statistics.usecases import Analyze

router = APIRouter(prefix="/analyze_sales", tags=["analyze"])


@router.post(
    "/",
    response_model=ReportDTO,
    summary="Analyze Sales Performance",
    description=(
        "Processes raw sales data to generate a comprehensive financial report. "
        "Calculates total revenue, margins, and categorizes dishes by profitability. "
        "Also provides strategic business recommendations based on the analyzed metrics."
    ),
)
async def analyze_sales(
    dishes_stats: Annotated[
        DishStatisticsInput,
        Body(description="List of dish statistics and report metadata"),
    ],
    usecase: Annotated[Analyze, Depends(analyze_usecase)],
) -> ReportDTO:
    """
    Orchestrate the sales analysis process:

    1. Calculate global totals (Revenue, Margin).
    2. Sort and filter dishes by margin thresholds.
    3. Aggregate data by categories.
    4. Generate business insights through the infrastructure layer.
    """
    dishes_stats_entities = [
        DishStatistics.model_validate(d) for d in dishes_stats.sales
    ]
    report = await usecase.execute(dishes_stats_entities)
    return ReportDTO.model_validate(report)
