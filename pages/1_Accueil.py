import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏠 Accueil — Répartition des actifs")

# Mini univers de démo (on passera à 150 après)
df = pd.DataFrame({
    "Actif": ["AAPL", "MSFT", "NVDA", "SPY", "BTC-USD"],
    "Poids": [20, 20, 20, 25, 15]
})

fig = px.pie(df, names="Actif", values="Poids", hole=0.35)
st.plotly_chart(fig, use_container_width=True)

st.caption("Prochaine étape: charger 150 actifs + données de marché (yfinance) + recherche + fiche actif.")
