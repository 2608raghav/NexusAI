from fastapi import FastAPI

from .service import WeatherService


app = FastAPI(
    title="Weather Agent"
)


service = WeatherService()


@app.get("/")
def root():

    return {
        "message": "Weather Agent is running"
    }


@app.get("/weather")
def get_weather(city: str):

    return service.get_weather(city)