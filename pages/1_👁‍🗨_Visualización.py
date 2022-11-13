
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import joblib
import streamlit.components.v1 as components
import datetime
import streamlit as st
import pickle
import pandas as pd

def load_data():
    data = pd.read_pickle('DataFramesYModelos/df_principal.pkl')
    return data

df = load_data()



########### SIDEBAR ##########
with st.sidebar:

    ################# ENTRADAS DATOS A PRECEDIR ##############################
    st.markdown("# Visualizar accidentes")
    fechas = st.date_input("Ingrese rango de fechas", [datetime.date(2014,7,4), datetime.date(2020,8,31)], min_value=datetime.date(2014,7,4), max_value=datetime.date(2020,8,31))
    tipo = st.selectbox("tipo de accidente: ", 
                        ("Atropello", "Caída de Ocupante", "Choque", "Incendio", "Volcamiento", "Otro"))

###################
try:
    fecha1, fecha2 = fechas
    df_filtrado = df
    df_filtrado["FECHA"] = df_filtrado["FECHA"].apply(lambda x: x.date())
    df_filtrado = df[(df["FECHA"]<=fecha2) & (df["FECHA"]>=fecha1) & (df["CLASE_ACCIDENTE"]==tipo)]
    st.write(df_filtrado)
except:
    st.markdown("# Esperando rango de fechas...")

