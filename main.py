from fastapi import FastAPI

from api.v1.analyze_rout import router as analyze_routes

app = FastAPI()


app.include_router(analyze_routes)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
