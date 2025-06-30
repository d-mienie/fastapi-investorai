from fastapi import APIRouter, Query
from app.services.finance import get_stock_summary, get_historical_prices

router = APIRouter()

@router.get("/")
def stock_summary(ticker: str = Query(...)):
    return get_stock_summary(ticker)

@router.get("/history")
def stock_history(
    ticker: str = Query(...),
    period: str = Query("1mo", description="e.g. 1d, 5d, 1mo, 3mo, 1y"),
    interval: str = Query("1d", description="e.g. 1m, 5m, 1d, 1wk")
):
    return get_historical_prices(ticker, period, interval)

