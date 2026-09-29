import httpx


class GatewayService:

    def __init__(self):

        self.orchestrator_url = "http://127.0.0.1:8000"

    def process_query(self, query: str):

        try:

            response = httpx.get(
                f"{self.orchestrator_url}/query",
                params={
                    "query": query
                },
                timeout=120.0
            )

            response.raise_for_status()

            return response.json()

        except httpx.TimeoutException:

            return {
                "error": "Orchestrator request timed out"
            }

        except httpx.RequestError:

            return {
                "error": "Could not connect to Orchestrator"
            }