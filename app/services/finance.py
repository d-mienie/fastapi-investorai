import yfinance as yf

def get_stock_summary(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info

    if "currentPrice" not in info:
        return {"error": f"No data found for {ticker}"}

    return {
        "symbol": info.get("symbol"),
        "name": info.get("shortName"),
        "price": info.get("currentPrice"),
        "52_week_high": info.get("fiftyTwoWeekHigh"),
        "52_week_low": info.get("fiftyTwoWeekLow"),
        "market_cap": info.get("marketCap"),
        "currency": info.get("currency")
    }

def get_historical_prices(ticker: str, period: str = "1mo", interval: str = "1d"):
    stock = yf.Ticker(ticker)
    history = stock.history(period=period, interval=interval)

    if history.empty:
        return {"error": f"No historical data for {ticker}"}

    # Convert to list of dicts
    return {
        "ticker": ticker.upper(),
        "data": history.reset_index().to_dict(orient="records")
    }

