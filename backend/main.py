from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api.routers import health
from core.logging import configure_logging, get_logger
from core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging(settings.log_level)
    logger = get_logger(__name__)
    logger.info("Starting %s (environment=%s)", settings.app_name, settings.environment)
    yield
    logger.info("Shutting down %s", settings.app_name)


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    lifespan=lifespan,
)

app.include_router(health.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug,
    )
