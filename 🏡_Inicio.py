import streamlit as st

st.set_page_config(page_title="Accidentes Med", page_icon="./Graficas/stockfish.png", layout="wide", initial_sidebar_state="auto")


st.title("Accidentalidad pasada y futura en Medellín")

st.markdown("""¡Bienvenido! Esta aplicación le ayudará a conocer datos útiles sobre accidentes
pasados y futuros en la ciudad de medellín. La página está dirigida especialmente a personas
que trabajen en prevensión de riesgos que puedan utilizar dichos datos para evitar futuros accidentes, 
así como comparar los accidentes que se materialicen en el mundo real con los predichos por la aplicación. Para comenzar, 
puede acceder a una de las pestañas de visualización, predicción o agrupamiento.
\n
Visualización: permite seleccionar una ventana de tiempo y obtener los datos históricos de accidentalidad
 por tipo de accidente.
\n
Predicción: permite predecir la accidentalidad por tipo de accidente dada una ventana de tiempo por fuera de
 los datos históricos.
\n
Agrupamiento: Permite visualizar un mapa de la ciudad en el cual se discrimina cada barrio en uno de 3 grupos de
 accidentalidad. Seleccionando un barrio se pueden ver las características del barrio y de su grupo.
            """)

st.markdown("Para detalles técnicos sobre el desarrollo de la aplicación, dirigirse a: https://github.com/eporrasm/TAE-trabajo3")
