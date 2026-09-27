import httpx

from shared.config.settings import settings


class NewsService:

    BASE_URL = "https://newsapi.org/v2/everything"

    def get_news(self, topic: str):

        params = {
            "q": topic,
            "apiKey": settings.NEWS_API_KEY,
            "language": "en",
            "pageSize": 5
        }

        response = httpx.get(
            self.BASE_URL,
            params=params
        )

        if response.status_code != 200:
            return {
                "error": response.text
            }

        data = response.json()

        articles = []

        for article in data["articles"]:

            articles.append({
                "title": article["title"],
                "source": article["source"]["name"],
                "url": article["url"]
            })

        return articles