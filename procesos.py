import streamlit as st
import pickle
import pandas as pd
import folium
import numpy as np

@st.cache
def load_df_clusters():
    
    #file = open("DataFramesYModelos/Clusters_Barrios.pkl",'rb')
    data = pd.read_pickle('DataFramesYModelos/Clusters_Barrios.pkl')
    #data = pickle.load(file)
    puntos = data[['LONGITUD','LATITUD','BARRIO','cluster']]

    return puntos



def llenar_mapa(MapaFrame, Cluster_0, Cluster_1, Cluster_2):
    
    for i in range(0,len(MapaFrame)):
        html = f"""<b>Nombre: </b> {MapaFrame.iloc[i]['BARRIO']} <br> 
                    <b>Atropello: </b> {MapaFrame.iloc[i]['Atropello_Accidentes']} <br>
                    <b>Caída de ocupante: </b> {MapaFrame.iloc[i]['Caída de Ocupante_Accidentes']} <br>
                    <b>Choque: </b> {MapaFrame.iloc[i]['Choque_Accidentes']} <br>
                    <b>Volcamiento: </b> {MapaFrame.iloc[i]['Volcamiento_Accidentes']} <br>
                    <b>Incendio: </b> {MapaFrame.iloc[i]['Incendio_Accidentes']} <br>
                    <b>Otro: </b> {MapaFrame.iloc[i]['Otro_Accidentes']}"""
        iframe = folium.IFrame(html)
        popup = folium.Popup(iframe, min_width=250, max_width=300)
        if MapaFrame.iloc[i]['cluster'] == 0: 
            color1 = "blue"
            Cluster_0.add_child(folium.Marker(
                location=[MapaFrame.iloc[i]['LATITUD'], MapaFrame.iloc[i]['LONGITUD']],
                icon=folium.Icon(color=color1) , popup = popup))
        elif MapaFrame.iloc[i]['cluster'] == 1:
            color1 = "green"
            Cluster_1.add_child(folium.Marker(
                location=[MapaFrame.iloc[i]['LATITUD'], MapaFrame.iloc[i]['LONGITUD']],
                icon=folium.Icon(color=color1) , popup = popup))
        else:
            color1 = "red"
            Cluster_2.add_child(folium.Marker(
                location=[MapaFrame.iloc[i]['LATITUD'], MapaFrame.iloc[i]['LONGITUD']],
                icon=folium.Icon(color=color1) , popup = popup))

@st.cache
def mpoint(lat, lon):
    return (np.average(lat), np.average(lon))

def create_map():
    #TODO: Características de cada punto en el mapa
    MapaFrame = load_df_agrupado_clusters()
    m = folium.Map(location=mpoint(MapaFrame["LATITUD"], MapaFrame["LONGITUD"]), tiles="OpenStreetMap", zoom_start=12)
    folium.TileLayer('stamenterrain').add_to(m)

    

    Cluster_0 = folium.FeatureGroup(name="Cluster 0").add_to(m)
    Cluster_1 = folium.FeatureGroup(name="Cluster 1").add_to(m)
    Cluster_2 = folium.FeatureGroup(name="Cluster 2").add_to(m)


    folium.LayerControl().add_to(m)
    
    llenar_mapa(MapaFrame, Cluster_0, Cluster_1, Cluster_2)
    
    return m

@st.cache
def load_df_agrupado_clusters():
    file = open("DataFramesYModelos/Clusters_Datos_Agrupados.pkl", "rb")
    Agrupado = pickle.load(file)
    return Agrupado

# file = open("DataFramesYModelos/Clusters_Datos_Agrupados.pkl", "rb")
# xd = pickle.load(file)
# print(xd)

#DATAFRAME AGRUPADO CLUSTERS#################################
# df = load_df_agrupado()
# df_clusters = load_df_clusters()

# newdf = pd.DataFrame()
# newdf["BARRIO"] = df["BARRIO"].unique()

# for accidente in df["CLASE_ACCIDENTE"].unique():
#     for categoria in ["Accidentes", "Heridos", "Daños", "Muertos"]:
#         temp = df[(df["CLASE_ACCIDENTE"] == accidente)][["BARRIO", categoria]]
#         newdf = newdf.merge(temp, on="BARRIO", how="left")
#         newdf.columns = [*newdf.columns[:-1], f"{accidente}_{categoria}"]
# newdf = newdf.replace({np.NaN: 0})
#newdf = df_clusters.merge(newdf,on="BARRIO", how="left")


# def predecir(valores):
#     valoresNorm = [normalizar("dep_inc_avg", valores[0]), normalizar("ind_inc_avg", valores[1]), normalizar("grad_debt_mdn", valores[2])]

#     df = pd.DataFrame([valoresNorm], columns=["DEP_INC_AVG", "IND_INC_AVG", "GRAD_DEBT_MDN"])
    
#     return modeloImport.predict(df)[0]


# @st.cache
# def mpoint(lat, lon):
#     return (np.average(lat), np.average(lon))
