import streamlit as st
from streamlit_folium import st_folium
from procesos import create_map

st.set_page_config(page_title="Agrupamiento Med", page_icon="./Graficas/stockfish.png", layout="wide", initial_sidebar_state="auto")

st.title("Agrupamiento de barrios")

Mapa = create_map()

m_data = st_folium(Mapa, width = 1200)


