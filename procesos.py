import streamlit as st
import pickle
import pandas as pd
import folium

@st.cache
def load_df_clusters():
    
    #file = open("DataFramesYModelos/Clusters_Barrios.pkl",'rb')
    data = pd.read_pickle('DataFramesYModelos/Clusters_Barrios.pkl')
    #data = pickle.load(file)
    puntos = data[['LONGITUD','LATITUD','BARRIO','cluster']]

    return puntos

print(load_df_clusters())

def create_map():
    #TODO: Características de cada punto en el mapa
    m = folium.Map(location=[20,0], tiles="OpenStreetMap", zoom_start=2)
    folium.TileLayer('stamenterrain').add_to(m)

    MapaFrame = load_df_clusters()

    Cluser_0 = folium.FeatureGroup(name="Cluster 0").add_to(m)
    Cluser_1 = folium.FeatureGroup(name="Cluster 1").add_to(m)
    Cluser_2 = folium.FeatureGroup(name="Cluster 2").add_to(m)


    folium.LayerControl().add_to(m)

    for i in range(0,len(MapaFrame)):
        if MapaFrame.iloc[i]['cluster'] == 0: 
            color1 = "blue"
            Cluser_0.add_child(folium.Marker(
                location=[MapaFrame.iloc[i]['LATITUD'], MapaFrame.iloc[i]['LONGITUD']],
                icon=folium.Icon(color=color1) , popup = MapaFrame.iloc[i]['BARRIO']))
        elif MapaFrame.iloc[i]['cluster'] == 1:
            color1 = "green"
            Cluser_1.add_child(folium.Marker(
                location=[MapaFrame.iloc[i]['LATITUD'], MapaFrame.iloc[i]['LONGITUD']],
                icon=folium.Icon(color=color1) , popup = MapaFrame.iloc[i]['BARRIO']))
        else:
            color1 = "red"
            Cluser_2.add_child(folium.Marker(
                location=[MapaFrame.iloc[i]['LATITUD'], MapaFrame.iloc[i]['LONGITUD']],
                icon=folium.Icon(color=color1) , popup = MapaFrame.iloc[i]['BARRIO']))
    return m

# def normalizar(columna, valor):
#     return (valor - df_data[columna].min())/(df_data[columna].max() - df_data[columna].min())


# def predecir(valores):
#     valoresNorm = [normalizar("dep_inc_avg", valores[0]), normalizar("ind_inc_avg", valores[1]), normalizar("grad_debt_mdn", valores[2])]

#     df = pd.DataFrame([valoresNorm], columns=["DEP_INC_AVG", "IND_INC_AVG", "GRAD_DEBT_MDN"])
    
#     return modeloImport.predict(df)[0]


# @st.cache
# def mpoint(lat, lon):
#     return (np.average(lat), np.average(lon))

# def get_separation(dataframe):
#     control1 = dataframe[dataframe["control"] == 1]
#     control2 = dataframe[dataframe["control"] == 2]
#     control3 = dataframe[dataframe["control"] == 3]
#     return (control1, control2, control3)

# @st.cache
# def get_kmeans_model_separation():

#     data = joblib.load("DataPrincipalClusters.pkl")

#     cluster_0 = data[data['cluster'] == 0]
#     cluster_1 = data[data['cluster'] == 1]
#     cluster_2 = data[data['cluster'] == 2]

#     return (cluster_0, cluster_1, cluster_2)

# def devolver_layers(lista):
#     layers = list()
#     if lista[0]:
#         layers.append(pdk.Layer(
#         'ScatterplotLayer',
#             data=df1,
#             get_position=["longitude", "latitude"],
#             get_color='[255, 0, 0, 160]',
#             get_radius=POINT_RADIUS,
#             pickable=True,
#         ))
#     if lista[1]:
#         layers.append(pdk.Layer(
#         'ScatterplotLayer',
#             data=df2,
#             get_position=["longitude", "latitude"],
#             get_color='[0, 255, 0, 160]',
#             get_radius=POINT_RADIUS,
#             pickable=True,
#         ))
#     if lista[2]:
#         layers.append(pdk.Layer(
#         'ScatterplotLayer',
#             data=df3,
#             get_position=["longitude", "latitude"],
#             get_color='[0, 0, 255, 160]',
#             get_radius=POINT_RADIUS,
#             pickable=True,
#         ))
#     else:
#         pass
#     return layers


# def cargar_mapa():
#     r = pdk.Deck(
#     map_style="dark",
#     initial_view_state={
#         "latitude": puntoMedioVisual[0],
#         "longitude": puntoMedioVisual[1],
#         "zoom": 3,
#     },
#      layers = layers, 
#      tooltip={
#         'html': """<b>Nombre: </b> {instnm} <br> 
#                    <b>Ingreso medio de familias de estudiantes dependientes: $</b> {dep_inc_avg} <br>
#                    <b>Ingreso medio de estudiantes independientes: $</b> {ind_inc_avg} <br>
#                    <b>Media de endeudamiento: $</b> {grad_debt_mdn} <br>
#                    <b>Tipo de universidad: </b> {control}""",
#         'style': {
#             'color': 'white'
#         }
#     })

#     return r