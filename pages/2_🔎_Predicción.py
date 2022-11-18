import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import streamlit as st
import pandas as pd
from procesos import load_models, procesar_fechas
from procesos import piso_techo
import numpy as np
import random

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
    finicial= f1
    while f1 <= f2:
        df_fechas = df_fechas.append(pd.DataFrame({"FECHA": [f1]}))
        f1 += datetime.timedelta(days=1)   
    df_fechas=df_fechas.reset_index(drop=True) 

    df_fechas = procesar_fechas(df_fechas)
    #st.write(df_fechas)
    if tipo == "Atropello":
        predicciones = atropello.predict(df_fechas)
    elif tipo == "Caída de Ocupante":
        predicciones = caida.predict(df_fechas)
    elif tipo == "Choque":
        predicciones = choque.predict(df_fechas)
    elif tipo == "Incendio":
        predicciones = list()
        for _ in range(df_fechas.shape[0]):
            r = random.random()
            if r<=0.012438916037316748:
                predicciones.append(1)
            else:
                predicciones.append(0)
        predicciones = np.asarray(predicciones)
    elif tipo == "Volcamiento":
        predicciones = volcamiento.predict(df_fechas)
    elif tipo == "Otro":
        predicciones = otro.predict(df_fechas)
        predicciones = np.asarray(tuple(map(piso_techo, predicciones)))

    st.subheader(f'Entre el {finicial} y el {f2} habrán {int(np.sum(predicciones))} accidentes de tipo "{tipo}"\n')

# st.subheader("Separando los accidentes por el dia en el que ocurrieron, tenemos los siguientes resultados: \n")
# sns.set()
# fig1, ax1 = plt.subplots()
# ax1.bar([_ for _ in range(len(predicciones))],predicciones, edgecolor="blue")
# ax1.set_title("Accidentalidad por dia")
# ax1.set_xlabel("Días")
# ax1.set_ylabel("Número de incidentes")
# ax1.set_xticklabels(labels=[])
# fig1.align_labels()
# st.pyplot(fig1)
    

except:
    st.markdown("# Esperando rango de fechas...")