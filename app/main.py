from fastapi import FastAPI
from app.routes import news,market

app = FastAPI(title="InvestorAI")

app.include_router(news.router, prefix="/news", tags=["News"])
app.include_router(market.router, prefix="/market", tags=["Market"])

