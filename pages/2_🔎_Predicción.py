import streamlit as st
import datetime

st.header("Predicción de accidentes futuros")
with st.sidebar:
    st.markdown("# Predecir accidentes")
    fechas = st.date_input("Ingrese rango de fechas (AAAA/MM/DD)", [datetime.date(2021,1,1), datetime.date(2022,12,31)], min_value=datetime.date(2021,1,1), max_value=datetime.date(2022,12,31))
    tipo = st.selectbox("tipo de accidente: ", 
                        ("Atropello", "Caída de Ocupante", "Choque", "Incendio", "Volcamiento", "Otro"))
