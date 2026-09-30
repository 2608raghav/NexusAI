import os
import httpx

from dotenv import load_dotenv
from shared.core.base_agent import BaseAgent

load_dotenv()


class FinanceService(BaseAgent):

    def __init__(self):

        super().__init__(
            name="Finance Agent",
            version="1.0"
        )

        self.api_key = os.getenv("TWELVE_DATA_API_KEY")
        self.api_url = "https://api.twelvedata.com/price"

    def get_stock_price(self, symbol: str):

        print("Finance Agent received request")
        print("Stock Symbol:", symbol)

        if not self.api_key:

            return {
                "error": "Twelve Data API key is not configured"
            }

        try:

            response = httpx.get(
                self.api_url,
                params={
                    "symbol": symbol.upper(),
                    "apikey": self.api_key
                },
                timeout=30.0
            )

            response.raise_for_status()

            data = response.json()

            if "price" not in data:

                return {
                    "error": data.get(
                        "message",
                        "Could not retrieve stock price"
                    )
                }

            return {
                "status": "success",
                "symbol": symbol.upper(),
                "price": float(data["price"]),
                "currency": "USD"
            }

        except httpx.TimeoutException:

            return {
                "error": "Finance API request timed out"
            }

        except httpx.RequestError:

            return {
                "error": "Could not connect to Finance API"
            }