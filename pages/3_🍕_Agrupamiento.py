import streamlit as st
from streamlit_folium import st_folium
from procesos import create_map

#TODO: Características de cada punto en el mapa
Mapa = create_map()

m_data = st_folium(Mapa, width = 725)

