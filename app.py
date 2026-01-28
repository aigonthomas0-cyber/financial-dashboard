import streamlit as st

st.set_page_config(page_title="Dashboard financier", layout="wide")

st.title("📊 Dashboard financier")
st.write("Si tu vois ce message, le déploiement fonctionne 🎉")

col1, col2, col3 = st.columns(3)
col1.metric("Actifs suivis", 150)
col2.metric("Valeur totale (€)", "1 250 000")
col3.metric("Performance YTD", "+8.4 %")
