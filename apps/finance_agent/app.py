from fastapi import FastAPI

from .service import FinanceService


app = FastAPI(
    title="Finance Agent"
)


service = FinanceService()


@app.get("/")
def root():

    return {
        "message": "Finance Agent is running"
    }


@app.get("/stock")
def get_stock(symbol: str):

    return service.get_stock_price(symbol)