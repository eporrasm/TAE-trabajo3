import streamlit as st
import pickle
import pandas as pd
import folium
import numpy as np
import datetime
import random

@st.cache
def load_df_clusters():
    
    #file = open("DataFramesYModelos/Clusters_Barrios.pkl",'rb')
    data = pd.read_pickle('DataFramesYModelos/Clusters_Barrios.pkl')
    #data = pickle.load(file)
    puntos = data[['LONGITUD','LATITUD','BARRIO','cluster']]

    return puntos

def load_data():
    data = pd.read_pickle('DataFramesYModelos/df_principal.pkl')
    return data

def llenar_mapa(MapaFrame, Cluster_0, Cluster_1, Cluster_2):
    
    for i in range(0,len(MapaFrame)):
        html = f""" <br>
                    <b>Atropellos: </b> {MapaFrame.iloc[i]['Atropello_Accidentes']} <br>
                    <b>Caídas de ocupante: </b> {MapaFrame.iloc[i]['Caída de Ocupante_Accidentes']} <br>
                    <b>Choques: </b> {MapaFrame.iloc[i]['Choque_Accidentes']} <br>
                    <b>Volcamientos: </b> {MapaFrame.iloc[i]['Volcamiento_Accidentes']} <br>
                    <b>Incendios: </b> {MapaFrame.iloc[i]['Incendio_Accidentes']} <br>
                    <b>Otros: </b> {MapaFrame.iloc[i]['Otro_Accidentes']}<br>
                    <b>Lugar más frecuente: </b> {MapaFrame.iloc[i]['DISEÑO']} <br>
                    <b>Momento más frecuente: </b> {MapaFrame.iloc[i]['MOMENTO']} <br>
                    <b>Gravedad más frecuente: </b> {MapaFrame.iloc[i]['GRAVEDAD_ACCIDENTE']} <br>
                    <b>Media Accidentes: </b> {round(MapaFrame.iloc[i]['Accidentes'],2)} <br>
                    <b>Media Heridos: </b> {round(MapaFrame.iloc[i]['Heridos'],2)} <br>
                    <b>Media Daños: </b> {round(MapaFrame.iloc[i]['Daños'],2)} <br>
                    <b>Media Muertos: </b> {round(MapaFrame.iloc[i]['Muertos'],2)}"""
        
        iframe = folium.IFrame(html)
        popup = folium.Popup(iframe, min_width=350, max_width=500)
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

    

    Cluster_0 = folium.FeatureGroup(name="Accidentalidad Baja").add_to(m)
    Cluster_1 = folium.FeatureGroup(name="Accidentalidad Media").add_to(m)
    Cluster_2 = folium.FeatureGroup(name="Accidentalidad Alta").add_to(m)


    folium.LayerControl().add_to(m)
    
    llenar_mapa(MapaFrame, Cluster_0, Cluster_1, Cluster_2)
    
    return m

@st.cache
def load_df_agrupado_clusters():

    file = open("DataFramesYModelos/Clusters_Datos_Agrupados_Definitivo.pkl", "rb")
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
    return atropello, caida, choque, otro, volcamiento

def quincena(f):
    z = []
    for i,j in zip(f['DayMo'],f['Dayw']):
        if (i in [15,30,31] and j in ['Monday','Tuesday', 'Thursday', 'Friday','Wednesday']):
            z.append(1)
        else:
            z.append(0)
    return z


def festivos():
    data = pd.read_excel("Festivos.xlsx")
    return data

def date_a_datetime(date):
    datetimef = datetime.datetime(year = date.year, month=date.month, day=date.day)
    return datetimef

def procesar_fechas(df_fechas):
    df_festivos = festivos()
    df_fechas["FECHA"] = df_fechas["FECHA"].apply(date_a_datetime)
    df_fechas['festivo'] = df_fechas['FECHA'].apply(lambda x: 1 if x in df_festivos['Fecha'].unique() else 0)
    df_fechas['Year'] = df_fechas['FECHA'].dt.year
    df_fechas['Month'] = df_fechas['FECHA'].dt.month
    df_fechas['DayMo'] = df_fechas['FECHA'].dt.day
    df_fechas['Dayw'] = df_fechas['FECHA'].apply(lambda x: x.strftime('%A'))
    df_fechas['Quincena'] = quincena(df_fechas)
    df_fechas.drop(["FECHA"], axis=1, inplace=True)
    df_fechas = pd.get_dummies(df_fechas)
    return df_fechas


# data = load_data()
# print(len(data[data["CLASE_ACCIDENTE"] == "Atropello"]), len(data[data["CLASE_ACCIDENTE"]== "Otro"]))

def piso_techo(num):
    coso = random.random()
    if coso < 0.5:
        return int(num)
    else:
        return int(num)+1
# df = load_data()
# df_clusters = df[['BARRIO','DIA_DEL_MES','MES','DISEÑO','MOMENTO','GRAVEDAD_ACCIDENTE']]
# df_clusters['BARRIO'] = df_clusters['BARRIO'].apply(lambda x : x.lower().replace("` ",""))
# df_clusters1 = df_clusters.groupby(['BARRIO','MES','DIA_DEL_MES'])["DISEÑO", "MOMENTO", 'GRAVEDAD_ACCIDENTE'].agg({"DISEÑO":lambda x: x.value_counts().index[0], "MOMENTO":lambda x: x.value_counts().index[0], "GRAVEDAD_ACCIDENTE":lambda x: x.value_counts().index[0]})
# df_clusters1 = df_clusters1.groupby('BARRIO').agg({"DISEÑO":lambda x: x.value_counts().index[0], "MOMENTO":lambda x: x.value_counts().index[0], "GRAVEDAD_ACCIDENTE":lambda x: x.value_counts().index[0]}).reset_index()



# # df2 = load_df_clusters()
# # print(df2)
# df_clusters_viejo = load_df_clusters()
# df_clusters1["cluster"] = df_clusters_viejo["cluster"]
# print("-----------------------------------------------------------------------")
# print(df_clusters1)


# df_clusters2 = df[['BARRIO','DIA_DEL_MES','MES','GRAVEDAD_ACCIDENTE']]
# df_clusters2["BARRIO"] = df_clusters2['BARRIO'].apply(lambda x : x.lower().replace("` ",""))
# df_clusters2 = df_clusters2.groupby(['BARRIO','MES','DIA_DEL_MES'])['GRAVEDAD_ACCIDENTE'].agg(([lambda x : x.count()  ,lambda x: ((x.__eq__('Con heridos')).sum()) , lambda x: ((x.__eq__('Solo daños')).sum()) ,lambda x: ((x.__eq__('Con muertos')).sum())]))
# df_clusters2 = df_clusters2.groupby(['BARRIO']).mean()
# df_clusters2.reset_index(inplace = True)
# df_clusters2.rename({df_clusters2.columns[1] :'Accidentes', df_clusters2.columns[2] : 'Heridos', df_clusters2.columns[3]: 'Daños', df_clusters2.columns[4]: 'Muertos'}, axis = 1, inplace = True)
# #print(df_clusters2)

# df3 = load_df_agrupado_clusters()
# #print(df3)

# newdf = pd.merge(df3, df_clusters1.drop(columns=["cluster"]), how="left", on="BARRIO")
# print("-----------------------------------------------------------------------")
# print(newdf)
# #print(df_clusters2)


# #print(df_clusters_viejo)

# df_clusters2["cluster"] = df_clusters_viejo["cluster"]
# #print(df_clusters2)

# newnewdf = df_clusters2.groupby("cluster", as_index=False).mean()
# print("-----------------------------------------------------------------------")
# newdf = newdf.merge(newnewdf, how="left", on="cluster")
# print(newdf)

#file = open("DataFramesYModelos/Clusters_Datos_Agrupados_Definitivo.pkl", "rb")
#Agrupado = pickle.load(file)

#print(Agrupado)




#df_clusters_viejo = df_clusters_viejo.merge(df_clusters2, on="BARRIO", how="left")
#df_clusters_viejo = df_clusters_viejo.groupby("cluster", as_index=False).mean()
#df_clusters_viejo = df_clusters_viejo[["cluster","Accidentes", "Heridos", "Daños", "Muertos"]]
#print(df_clusters_viejo)



#df_con_means = df_clusters2.merge(df_clusters_viejo, on="cluster", how="left")
#print(df_con_means)

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
