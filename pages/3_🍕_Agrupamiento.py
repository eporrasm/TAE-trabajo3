import streamlit as st
from streamlit_folium import st_folium
from procesos import create_map
import streamlit.components.v1 as components

st.set_page_config(page_title="Agrupamiento Med", page_icon="./Graficas/stockfish.png", layout="wide", initial_sidebar_state="auto")

st.title("Agrupamiento de barrios")

#Mapa = create_map()

#Mapa.save("Graficas/MapaFinal.html")

#m_data = st_folium(Mapa, width = 1200)

HtmlFile = open("Graficas/MapaFinal.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, width=1200, height=700)


