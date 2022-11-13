# import streamlit as st
# import joblib

# def load_data():
    
#     data = joblib.load("DataPrincipal.pkl")

#     return data

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