from fastapi import FastAPI

from shared.config.settings import settings
from shared.models.health import HealthResponse

from .service import OrchestratorService


# =====================================================
# CREATE FASTAPI APPLICATION
# =====================================================

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


# =====================================================
# CREATE ORCHESTRATOR SERVICE
# =====================================================

service = OrchestratorService()


# =====================================================
# ROOT ENDPOINT
# =====================================================

@app.get("/")
def root():

    return {
        "message": "Welcome to NexusAI Orchestrator Agent"
    }


# =====================================================
# HEALTH CHECK
# =====================================================

@app.get(
    "/health",
    response_model=HealthResponse
)
def health():

    return service.health()


# =====================================================
# DIRECT NEWS ENDPOINT
# =====================================================

@app.get("/news")
def get_news(topic: str):

    return service.get_news(topic)


# =====================================================
# DIRECT WEATHER ENDPOINT
# =====================================================

@app.get("/weather")
def get_weather(city: str):

    return service.get_weather(city)


# =====================================================
# LLM POWERED QUERY
# =====================================================

@app.get("/query")
def handle_query(query: str):

    return service.process_query(query)