from fastapi import FastAPI
from app.routes import news

app = FastAPI(title="InvestorAI")

app.include_router(news.router, prefix="/news", tags=["News"])

