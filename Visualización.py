
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import joblib
import streamlit.components.v1 as components

st.set_page_config(page_title="Universingreso", page_icon="./Graficas/stockfish.png", layout="centered", initial_sidebar_state="auto")

descripcion = False
DESCRIPCIONES = ("""# Cluster 1.
- Es el cluster con mayor cantidad de universidades, con un total de 3174 universidades.
- Se caracteriza por tener las deudas más bajas, donde la media de la deuda se encuentra en \$10 201 USD y el 75\% de los estudiantes tienen una deuda menor a \$12 000 USD. 
- El salario promedio de los estudiantes dependientes es de \$39 530 USD y de \$17 255   (tanto los dependientes como los independientes). Estos salarios son similares a los del cluster 3 y menores a los del cluster 2.""",
                """ # Cluster 2.
- Tiene 1409 universidades.
- Se destacan los salarios altos, con una media de \$80 211 USD, donde tan solo el 25\% de los estudiantes gana menos de \$68 000 USD en estudiantes dependientes, y con una media de \$27 233 USD en estudiantes independientes. 
- Se caracteriza por tener una gran cantidad de universidades privadas sin ánimo de lucro. Tiene 868 de 1301 universidades con esta estructura de gobierno de la institución, es decir, un 67%.""",
                """ # Cluster 3.
- Tiene 1120 universidades, lo que lo hace el cluster más pequeño.
- Como se puede observar en la figura 3D y los datos, el cluster es semejante al cluster 1 pero las deudas son, en general, más altas. Véase que los salarios son más bajos que en Cluster 2, con una media de \$40 701 USD en estudiantes dependientes y \$19 174 USD en estudiantes dependientes. Sin embargo, la deuda haciende a una media de \$26 499 USD, más alta que la de los estudiantes del Cluster 2, que es, en promedio, de \$23251 USD.
- El 75\% de los estudiantes tiene una deuda superior a \$21599.0 USD que es mayor a la deuda máxima entre los estudiantes de las universidades del cluster 2, que es de \$18833 USD.""")

POINT_RADIUS = 10000


def load_data():
    
    data = joblib.load("DataPrincipal.pkl")

    return data

def normalizar(columna, valor):
    return (valor - df_data[columna].min())/(df_data[columna].max() - df_data[columna].min())


def predecir(valores):
    valoresNorm = [normalizar("dep_inc_avg", valores[0]), normalizar("ind_inc_avg", valores[1]), normalizar("grad_debt_mdn", valores[2])]

    df = pd.DataFrame([valoresNorm], columns=["DEP_INC_AVG", "IND_INC_AVG", "GRAD_DEBT_MDN"])
    
    return modeloImport.predict(df)[0]


@st.cache
def mpoint(lat, lon):
    return (np.average(lat), np.average(lon))

def get_separation(dataframe):
    control1 = dataframe[dataframe["control"] == 1]
    control2 = dataframe[dataframe["control"] == 2]
    control3 = dataframe[dataframe["control"] == 3]
    return (control1, control2, control3)

@st.cache
def get_kmeans_model_separation():

    data = joblib.load("DataPrincipalClusters.pkl")

    cluster_0 = data[data['cluster'] == 0]
    cluster_1 = data[data['cluster'] == 1]
    cluster_2 = data[data['cluster'] == 2]

    return (cluster_0, cluster_1, cluster_2)

def devolver_layers(lista):
    layers = list()
    if lista[0]:
        layers.append(pdk.Layer(
        'ScatterplotLayer',
            data=df1,
            get_position=["longitude", "latitude"],
            get_color='[255, 0, 0, 160]',
            get_radius=POINT_RADIUS,
            pickable=True,
        ))
    if lista[1]:
        layers.append(pdk.Layer(
        'ScatterplotLayer',
            data=df2,
            get_position=["longitude", "latitude"],
            get_color='[0, 255, 0, 160]',
            get_radius=POINT_RADIUS,
            pickable=True,
        ))
    if lista[2]:
        layers.append(pdk.Layer(
        'ScatterplotLayer',
            data=df3,
            get_position=["longitude", "latitude"],
            get_color='[0, 0, 255, 160]',
            get_radius=POINT_RADIUS,
            pickable=True,
        ))
    else:
        pass
    return layers


def cargar_mapa():
    r = pdk.Deck(
    map_style="dark",
    initial_view_state={
        "latitude": puntoMedioVisual[0],
        "longitude": puntoMedioVisual[1],
        "zoom": 3,
    },
     layers = layers, 
     tooltip={
        'html': """<b>Nombre: </b> {instnm} <br> 
                   <b>Ingreso medio de familias de estudiantes dependientes: $</b> {dep_inc_avg} <br>
                   <b>Ingreso medio de estudiantes independientes: $</b> {ind_inc_avg} <br>
                   <b>Media de endeudamiento: $</b> {grad_debt_mdn} <br>
                   <b>Tipo de universidad: </b> {control}""",
        'style': {
            'color': 'white'
        }
    })

    return r


st.title("Universingreso")

st.markdown("""¡Bienvenido! Esta aplicación le ayudará a tomar una decisión 
            en cuanto a su elección de universidad en Estados Unidos. Para comenzar, simplemente
            utilice el formulario de la izquierda para especificar su dependencia/independencia, el ingreso de su familia y 
            la déuda máxima que desea asumir al final de sus estudios. La página le arrojará un conjunto de universidades recomendado
            que puede visualizar en el mapa. Si desea ver más o menos grupos de universidades, simplemente marque
            o desmarque los botones seleccionables de la parte inferior izquierda.""")

######## DATAFRAME PRINCIPAL #########
df_data = load_data()
##################################

df1, df2, df3 = get_kmeans_model_separation()

modeloImport = joblib.load("classifier.joblib")



########### SIDEBAR ##########
with st.sidebar:

    ################# ENTRADAS DATOS A PRECEDIR ##############################
    st.markdown("# Datos de nueva entrada para predecir")

    st.write("Es usted dependiente o independiente del salario de su familia?")
    dependencia = st.radio(label="Escoja: ",
             options=("Dependiente", "Independiente"))

    if dependencia == "Dependiente":

        dep_avg = st.slider(
            "Ingreso de su familia en dólares",
            float(df_data["dep_inc_avg"].min()), 
            float(df_data["dep_inc_avg"].max()), 
            float(df_data["dep_inc_avg"].mean())
        )

        ind_avg = float(df_data["ind_inc_avg"].min())
    else:

        ind_avg = st.slider(
            "Ingreso de su familia en dólares",
            float(df_data["ind_inc_avg"].min()), 
            float(df_data["ind_inc_avg"].max()), 
            float(df_data["ind_inc_avg"].mean())
        )

        dep_avg = float(df_data["dep_inc_avg"].min())

    grad_mdn = st.slider(
        "Deuda total en dólares que desea asumir al final de sus estudios",
        float(df_data["grad_debt_mdn"].min()), 
        float(df_data["grad_debt_mdn"].max()), 
        float(df_data["grad_debt_mdn"].mean())
    )
    ############################################################

    if st.button("Predecir cluster de los valores"):
        descripcion = True
    
    ############# CHECKS #####################
    st.write("                      ")
    st.markdown("# Clusters a mostrar")
    
    st.markdown("Solo se mostrarán los clusters que estén marcados en el momento.")

    cluster1 = st.checkbox("Mostrar cluster 1 (rojo)", value = True)
    cluster2 = st.checkbox("Mostrar cluster 2 (verde)", value = True)
    cluster3 = st.checkbox("Mostrar cluster 3 (azul)", value = True)

    layers = devolver_layers([cluster1, cluster2, cluster3])
    puntoMedioVisual = mpoint(df_data["latitude"], df_data["longitude"])
    ##########################################
#############################

if not descripcion:
    st.subheader("Mapa de los clusters")
    st.write("""Para ver las características de cada universidad, simplemente pasar el cursor sobre ella.\nSe recomienda utilizar la rueda del ratón para acercar y alejar el mapa.""")
    components.html(cargar_mapa().to_html(as_string=True), width=600, height=600)

else:
    st.subheader("Descripción del cluster predecido")
    st.markdown(DESCRIPCIONES[predecir([dep_avg, ind_avg, grad_mdn])])
    st.subheader("Mapa de los clusters")
    st.write("""Para ver las características de cada universidad, simplemente pasar el cursor sobre ella.\nSe recomienda utilizar la rueda del ratón para acercar y alejar el mapa.""")
    components.html(cargar_mapa().to_html(as_string=True), width=600, height=600)
        
