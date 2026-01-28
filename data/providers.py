import pandas as pd
import yfinance as yf
import streamlit as st

def _clean(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        return pd.DataFrame()
    df = df.reset_index()
    df.columns = [c.lower() for c in df.columns]
    if "date" not in df.columns and "datetime" in df.columns:
        df = df.rename(columns={"datetime": "date"})
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    for c in ["open","high","low","close","adj close","volume"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    if "adj close" in df.columns and "adj_close" not in df.columns:
        df = df.rename(columns={"adj close":"adj_close"})
    return df.dropna(subset=["date"])

@st.cache_data(ttl=300)
def get_history(ticker: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    df = yf.download(
        tickers=ticker,
        period=period,
        interval=interval,
        progress=False,
        threads=False,
        auto_adjust=False,
    )
    return _clean(df)
