import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.title("🔎 Fiche Actif")

ticker = st.text_input("Ticker (ex: AAPL, MSFT, SPY, BTC-USD)", "AAPL").strip()

period = st.selectbox("Période", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=3)

@st.cache_data(ttl=300)
def load_prices(ticker: str, period: str):
    df = yf.download(ticker, period=period, interval="1d", progress=False)
    if df is None or df.empty:
        return pd.DataFrame()
    df = df.reset_index()
    df.columns = [c.lower() for c in df.columns]
    return df

df = load_prices(ticker, period)

if df.empty:
    st.error("Aucune donnée trouvée pour ce ticker. Essaie un autre (ex: SPY, MSFT, BTC-USD).")
    st.stop()

last = float(df["close"].iloc[-1])
first = float(df["close"].iloc[0])
perf = (last / first - 1) * 100

c1, c2 = st.columns(2)
c1.metric("Dernier cours", f"{last:,.2f}")
c2.metric("Performance période", f"{perf:,.2f}%")

fig = px.line(df, x="date", y="close", title=f"Cours — {ticker}")
st.plotly_chart(fig, use_container_width=True)

st.dataframe(df.tail(20), use_container_width=True)
