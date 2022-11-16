import streamlit as st
import pickle
import pandas as pd
import folium
import numpy as np
import datetime

@st.cache
def load_df_clusters():
    
    #file = open("DataFramesYModelos/Clusters_Barrios.pkl",'rb')
    data = pd.read_pickle('DataFramesYModelos/Clusters_Barrios.pkl')
    #data = pickle.load(file)
    puntos = data[['LONGITUD','LATITUD','BARRIO','cluster']]

    return puntos



def llenar_mapa(MapaFrame, Cluster_0, Cluster_1, Cluster_2):
    
    for i in range(0,len(MapaFrame)):
        html = f"""<b>Accidentes: </b> Cantidad <br> 
                    <br>
                    <b>Atropello: </b> {MapaFrame.iloc[i]['Atropello_Accidentes']} <br>
                    <b>Caída de ocupante: </b> {MapaFrame.iloc[i]['Caída de Ocupante_Accidentes']} <br>
                    <b>Choque: </b> {MapaFrame.iloc[i]['Choque_Accidentes']} <br>
                    <b>Volcamiento: </b> {MapaFrame.iloc[i]['Volcamiento_Accidentes']} <br>
                    <b>Incendio: </b> {MapaFrame.iloc[i]['Incendio_Accidentes']} <br>
                    <b>Otro: </b> {MapaFrame.iloc[i]['Otro_Accidentes']}"""
        
        iframe = folium.IFrame(html)
        popup = folium.Popup(iframe, min_width=270, max_width=300)
        if MapaFrame.iloc[i]['cluster'] == 0: 
            color1 = "blue"
            Cluster_0.add_child(folium.Marker(
                location=[MapaFrame.iloc[i]['LATITUD'], MapaFrame.iloc[i]['LONGITUD']],
                tooltip= f"{MapaFrame.iloc[i]['BARRIO']}",
                icon=folium.Icon(color=color1) , popup = popup))
        elif MapaFrame.iloc[i]['cluster'] == 1:
            color1 = "green"
            Cluster_1.add_child(folium.Marker(
                location=[MapaFrame.iloc[i]['LATITUD'], MapaFrame.iloc[i]['LONGITUD']],
                tooltip= f"{MapaFrame.iloc[i]['BARRIO']}",
                icon=folium.Icon(color=color1) , popup = popup))
        else:
            color1 = "red"
            Cluster_2.add_child(folium.Marker(
                location=[MapaFrame.iloc[i]['LATITUD'], MapaFrame.iloc[i]['LONGITUD']],
                tooltip= f"{MapaFrame.iloc[i]['BARRIO']}",
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


def load_models():
    atropello = open("DataFramesYModelos/modelo_Atropello_entrenado.pkl",'rb')
    caida =  open('DataFramesYModelos/modelo_Caida_entrenado.pkl','rb')
    choque =  open('DataFramesYModelos/modelo_choque_entrenado.pkl','rb')
    otro =  open('DataFramesYModelos/modelo_Otro_entrenado.pkl','rb')
    volcamiento =  open('DataFramesYModelos/modelo_Volcamiento_entrenado.pkl','rb')
    atropello = pickle.load(atropello)
    caida =  pickle.load(caida)
    choque =  pickle.load(choque)
    otro =  pickle.load(otro)
    volcamiento =  pickle.load(volcamiento)
    return (atropello, caida, choque, otro, volcamiento)

def quincena(f):
    z = []
    for i,j in zip(f['DayMo'],f['Dayw']):
        if (i in [15,30,31] and j in ['Monday','Tuesday', 'Thursday', 'Friday','Wednesday']):
            z.append(1)
        else:
            z.append(0)
    return z

@st.cache
def festivos():
    return pd.read_excel("Festivos.xlsx")


def procesar_fechas(df_fechas):
    df_festivos = festivos()
    df_fechas['festivo'] = df_fechas['FECHA'].apply(lambda x: 1 if x in df_festivos['Fecha'].unique() else 0)
    df_fechas['Year'] = df_fechas['FECHA'].dt.year
    df_fechas['Month'] = df_fechas['FECHA'].dt.month
    df_fechas['DayMo'] = df_fechas['FECHA'].dt.day
    df_fechas['Dayw'] = df_fechas['FECHA'].apply(lambda x: x.strftime('%A'))
    df_fechas['Quincena'] = quincena(df_fechas)
    df_fechas.drop(["FECHA"], axis=1, inplace=True)
    return df_fechas



# df4 = df[['BARRIO','DIA_DEL_MES','MES','GRAVEDAD_ACCIDENTE']]
# df4['BARRIO'] = df4['BARRIO'].apply(lambda x : x.lower().replace("` ",""))
# df4 = df4.groupby(['BARRIO','MES','DIA_DEL_MES'])['GRAVEDAD_ACCIDENTE'].agg(([lambda x : x.count()  ,lambda x: ((x.__eq__('Con heridos')).sum()) , lambda x: ((x.__eq__('Solo daños')).sum()) ,lambda x: ((x.__eq__('Con muertos')).sum())]))
# df4 = df4.groupby(['BARRIO']).mean()
# df4.reset_index(inplace = True)
# df4.rename({df4.columns[1] :'Accidentes', df4.columns[2] : 'Heridos', df4.columns[3]: 'Daños', df4.columns[4]: 'Muertos'}, axis = 1, inplace = True)


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
