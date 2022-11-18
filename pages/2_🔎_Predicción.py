import streamlit as st

import datetime
import streamlit as st
import pandas as pd
from procesos import load_models, procesar_fechas

st.title("Predicción de accidentes futuros")

atropello, caida, choque, otro, volcamiento = load_models()

with st.sidebar:
    st.markdown("# Predecir accidentes")
    fechas = st.date_input("Ingrese rango de fechas (AAAA/MM/DD)", [datetime.date(2021,1,1), datetime.date(2022,12,31)], min_value=datetime.date(2021,1,1), max_value=datetime.date(2022,12,31))
    tipo = st.selectbox("tipo de accidente: ", 
                        ("Atropello", "Caída de Ocupante", "Choque", "Incendio", "Volcamiento", "Otro"))
 #Hay que hacer un dataframe de una sola columna que se llama "FECHA" donde cada fila
 #es una fecha en el rango que dio el usuario. Después hay que aplicar procesar_fechas a
#este dataframe y ya queda con el formato para aplicar el modelo.

try:
    df_fechas = pd.DataFrame(columns=["FECHA"])
    f1,f2 = fechas
    while f1 <= f2:
        df_fechas = df_fechas.append(pd.DataFrame({"FECHA": [f1]}))
        f1 += datetime.timedelta(days=1)   
    df_fechas=df_fechas.reset_index(drop=True) 
    st.write(df_fechas)

except:
    st.markdown("# Esperando rango de fechas...")