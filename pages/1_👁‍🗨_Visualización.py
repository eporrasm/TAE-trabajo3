
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import datetime
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Accidentes Med", page_icon="./Graficas/stockfish.png", layout="wide", initial_sidebar_state="auto")

def load_data():
    data = pd.read_pickle('DataFramesYModelos/df_principal.pkl')
    return data





########### SIDEBAR ##########
with st.sidebar:

    ################# ENTRADAS DATOS A PRECEDIR ##############################
    st.markdown("# Visualizar accidentes")
    fechas = st.date_input("Ingrese rango de fechas (AAAA/MM/DD)", [datetime.date(2014,7,4), datetime.date(2020,8,31)], min_value=datetime.date(2014,7,4), max_value=datetime.date(2020,8,31))
    tipo = st.selectbox("tipo de accidente: ", 
                        ("Atropello", "Caída de Ocupante", "Choque", "Incendio", "Volcamiento", "Otro"))

###################
df = load_data()
sns.set()
try:
    st.header("Visualización de datos históricos")
    #Definición del df
    fecha1, fecha2 = fechas
    df_filtrado = df
    df_filtrado["FECHA"] = df_filtrado["FECHA"].apply(lambda x: x.date())
    df_filtrado = df[(df["FECHA"]<=fecha2) & (df["FECHA"]>=fecha1) & (df["CLASE_ACCIDENTE"]==tipo)]
    f1 = fecha1.strftime("%Y/%m/%d")
    f2 = fecha2.strftime("%Y/%m/%d")
    st.subheader(f'Entre el {f1} y el {f2} hubo {df_filtrado.shape[0]} accidentes de tipo "{tipo}"\n')
    #Plot diseño
    st.subheader("Separando los accidentes por el sitio en el que ocurrieron, tenemos los siguientes resultados: \n")
    fig1, ax1 = plt.subplots()
    ax1.hist(df_filtrado["DISEÑO"], bins=11, ec="black")
    ax1.set_title("Accidentalidad por sitio")
    ax1.set_xlabel("Lugar")
    ax1.set_ylabel("Número de incidentes")
    ax1.set_xticklabels(labels=df_filtrado["DISEÑO"].unique(),rotation=-90)
    fig1.align_labels()
    st.pyplot(fig1)
    #Plot gravedad
    st.subheader("En cuanto a la gravedad de los accidentes, se tiene: \n")
    fig2, ax2 = plt.subplots()
    ax2.hist(df_filtrado["GRAVEDAD_ACCIDENTE"], bins=11, ec="black")
    ax2.set_title("Gravedad de los accidentes")
    ax2.set_xlabel("Gravedad")
    ax2.set_ylabel("Número de incidentes")
    ax2.set_xticklabels(labels=df_filtrado["GRAVEDAD_ACCIDENTE"].unique(),rotation=-90)
    fig2.align_labels()
    st.pyplot(fig2)
    #Plot momento
    st.subheader("Es interesante visualizar en qué momento del día suelen ocurrir estos accidentes: \n")
    fig3, ax3 = plt.subplots()
    ax3.hist(df_filtrado["MOMENTO"], bins=11, ec="black")
    ax3.set_title("Accidentalidad según momento del día")
    ax3.set_xlabel("Momento del día")
    ax3.set_ylabel("Número de incidentes")
    ax3.set_xticklabels(labels=df_filtrado["MOMENTO"].unique(),rotation=-90)
    fig3.align_labels()
    st.pyplot(fig3)
except:
    st.markdown("# Esperando rango de fechas...")
   
