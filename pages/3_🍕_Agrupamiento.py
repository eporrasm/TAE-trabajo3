import streamlit as st
from streamlit_folium import st_folium
from procesos import create_map
from procesos import load_df_principal

st.header("Agrupamiento de barrios")
#TODO: Características de cada punto en el mapa
#Mapa = create_map()

#m_data = st_folium(Mapa, width = 725)

st.write(load_df_principal())

