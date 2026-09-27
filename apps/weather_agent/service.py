import httpx


class WeatherService:

    GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"

    WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self, city: str):

        # Step 1: Convert city name into coordinates

        geo_response = httpx.get(
            self.GEOCODING_URL,
            params={
                "name": city,
                "count": 1
            }
        )

        geo_data = geo_response.json()

        if "results" not in geo_data:
            return {
                "error": "City not found"
            }

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        # Step 2: Get weather using coordinates

        weather_response = httpx.get(
            self.WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m"
            }
        )

        weather_data = weather_response.json()

        current_weather = weather_data["current"]

        return {
            "city": location["name"],
            "country": location.get("country"),

            "temperature": current_weather["temperature_2m"],

            "apparent_temperature": current_weather["apparent_temperature"],

            "humidity": current_weather["relative_humidity_2m"],

            "wind_speed": current_weather["wind_speed_10m"],

            "weather_code": current_weather["weather_code"]
        }