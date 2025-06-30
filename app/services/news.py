import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_latest_news(limit=5):
    url = "https://finnhub.io/api/v1/news?category=general"
    params = {"token": os.getenv("FINNHUB_API_KEY")}
    response = requests.get(url, params=params)
    data = response.json()
    return [article["headline"] for article in data[:limit]]

