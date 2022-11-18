import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Agrupamiento Med", page_icon="./Graficas/stockfish.png", layout="wide", initial_sidebar_state="auto")

st.title("Agrupamiento de barrios")

HtmlFile = open("Graficas/MapaFinal.html", 'r')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, width=1200, height=700)


