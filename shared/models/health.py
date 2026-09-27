from pydantic import BaseModel


class HealthResponse(BaseModel):
    agent: str
    version: str
    status: str