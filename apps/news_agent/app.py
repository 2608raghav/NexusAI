from fastapi import FastAPI

from .service import NewsService


app = FastAPI(
    title="News Agent"
)


service = NewsService()


@app.get("/")
def root():

    return {
        "message": "News Agent is running"
    }


@app.get("/news")
def get_news(topic: str):

    return service.get_news(topic)