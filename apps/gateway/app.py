from fastapi import FastAPI

from .service import GatewayService


app = FastAPI(
    title="NexusAI Gateway"
)


service = GatewayService()


@app.get("/")
def root():

    return {
        "message": "NexusAI Gateway is running"
    }


@app.get("/query")
def query(query: str):

    return service.process_query(query)