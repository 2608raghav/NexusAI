import httpx
import json

from shared.core.base_agent import BaseAgent


class OrchestratorService(BaseAgent):

    def __init__(self):

        super().__init__(
            name="Orchestrator Agent",
            version="1.0"
        )

        self.news_agent_url = "http://127.0.0.1:8001"
        self.weather_agent_url = "http://127.0.0.1:8002"

        # Ollama
        self.ollama_url = "http://127.0.0.1:11434/api/chat"
        self.ollama_model = "qwen3:8b"


    # =====================================================
    # NEWS AGENT COMMUNICATION
    # =====================================================

    def get_news(self, topic: str):

        try:

            response = httpx.get(
                f"{self.news_agent_url}/news",
                params={
                    "topic": topic
                },
                timeout=120.0
            )

            response.raise_for_status()

            return response.json()

        except httpx.TimeoutException:

            return {
                "error": "News Agent request timed out"
            }

        except httpx.RequestError:

            return {
                "error": "Could not connect to News Agent"
            }


    # =====================================================
    # WEATHER AGENT COMMUNICATION
    # =====================================================

    def get_weather(self, city: str):

        try:

            response = httpx.get(
                f"{self.weather_agent_url}/weather",
                params={
                    "city": city
                },
                timeout=120.0
            )

            response.raise_for_status()

            return response.json()

        except httpx.TimeoutException:

            return {
                "error": "Weather Agent request timed out"
            }

        except httpx.RequestError:

            return {
                "error": "Could not connect to Weather Agent"
            }


    # =====================================================
    # LLM QUERY UNDERSTANDING
    # =====================================================

    def understand_query(self, query: str):

        prompt = f"""
You are the query understanding system for a multi-agent AI platform.

Available agents:

1. weather
   Handles weather, temperature, humidity, rain, wind and forecasts.

2. news
   Handles latest news, headlines, updates and current events.

3. unknown
   Use when the query does not belong to weather or news.


Available intents:

Weather:
- current_weather
- forecast

News:
- latest_news

Unknown:
- unknown


Return ONLY valid JSON in this exact format:

{{
    "agent": "weather or news or unknown",
    "intent": "current_weather or forecast or latest_news or unknown",
    "city": "city name or null",
    "topic": "news topic or null"
}}


Rules:

- If the user asks about current weather, use "current_weather".
- If the user asks about future weather or forecast, use "forecast".
- If the user asks for latest news, headlines or current events, use "latest_news".
- For weather queries, extract the city.
- For news queries, extract the news topic.
- If a city cannot be identified, use null.
- If a news topic cannot be identified, use null.
- Do not add explanations.
- Return JSON only.


User query:
{query}
"""

        try:

            print("Sending query to Ollama...")

            response = httpx.post(
                self.ollama_url,
                json={
                    "model": self.ollama_model,
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "stream": False,
                    "format": "json"
                },
                timeout=120.0
            )

            response.raise_for_status()

            data = response.json()

            content = data["message"]["content"]

            print("Ollama Response:", content)

            result = json.loads(content)

            return result

        except httpx.TimeoutException:

            return {
                "error": "Ollama request timed out"
            }

        except httpx.RequestError:

            return {
                "error": "Could not connect to Ollama"
            }

        except (KeyError, json.JSONDecodeError):

            return {
                "error": "Ollama returned an invalid response"
            }


    # =====================================================
    # PROCESS NATURAL LANGUAGE QUERY
    # =====================================================

    def process_query(self, query: str):

        # Ask LLM to understand the query

        result = self.understand_query(query)


        # Check if LLM failed

        if "error" in result:

            return result


        # Extract structured information

        agent = result.get("agent")
        intent = result.get("intent")
        city = result.get("city")
        topic = result.get("topic")


        print("User Query:", query)
        print("Agent:", agent)
        print("Intent:", intent)
        print("City:", city)
        print("Topic:", topic)


        # =================================================
        # WEATHER AGENT
        # =================================================

        if agent == "weather":

            if not city:

                return {
                    "error": "I could not identify the city"
                }


            # Currently our Weather Agent supports
            # current weather.

            if intent == "current_weather":

                return self.get_weather(city)


            # Forecast will be implemented later.

            if intent == "forecast":

                return {
                    "message": "Forecast support will be added soon."
                }


        # =================================================
        # NEWS AGENT
        # =================================================

        if agent == "news":

            if not topic:

                return {
                    "error": "I could not identify the news topic"
                }


            if intent == "latest_news":

                return self.get_news(topic)


        # =================================================
        # UNKNOWN
        # =================================================

        return {
            "error": "Sorry, I could not understand your request"
        }