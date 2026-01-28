import streamlit as st
import pandas as pd
import plotly.express as px

from data.universe import UNIVERSE_150
from data.providers import get_history
from data.indicators import (
    returns, cagr, volatility, max_drawdown,
    sharpe_ratio, summary
)

st.set_page_config(page_title="Fiche Actif", layout="wide")

st.title("📄 Fiche Actif")
st.caption("Analyse détaillée d’un actif financier")

# Sélection actif
ticker = st.selectbox(
    "Choisissez un actif",
    sorted(UNIVERSE_150),
    index=0
)

period = st.radio(
    "Période",
    ["6mo", "1y", "2y", "5y"],
    horizontal=True,
    index=1
)

# Récupération données
df = get_history(ticker, period=period)

if df.empty:
    st.warning("Données indisponibles pour cet actif.")
    st.stop()

close = df["close"].dropna()

# Graphique prix
fig_price = px.line(
    df,
    x=df.index,
    y="close",
    title=f"{ticker} — Évolution du prix"
)
st.plotly_chart(fig_price, use_container_width=True)

# KPIs
stats = summary(close)

k1, k2, k3, k4 = st.columns(4)
k1.metric("Performance totale", f"{stats['Perf totale']*100:.2f}%")
k2.metric("CAGR", f"{stats['CAGR']*100:.2f}%")
k3.metric("Volatilité", f"{stats['Vol annualisée']*100:.2f}%")
k4.metric("Max drawdown", f"{stats['Max drawdown']*100:.2f}%")

# Rendements
ret = returns(close)

fig_ret = px.histogram(
    ret.dropna(),
    nbins=50,
    title="Distribution des rendements"
)
st.plotly_chart(fig_ret, use_container_width=True)

# Tableau indicateurs
with st.expander("📊 Indicateurs détaillés"):
    st.dataframe(
        pd.DataFrame(stats, index=["Valeur"]).T,
        use_container_width=True
    )
