# Trabajo 2 de Técnicas en Aprendizaje Estadístico de la UNAL-med 

## A cargo de:

- Esteban García Carmona
- Emilio Porras Mejía
- Felipe Miranda Arboleda
- José Luis Suárez Ledesma

## Introducción 
En el presente informe se buscará tratar de predecir la accidentalidad en la ciudad de Medellín con base en la información de accidentes reportados a través de la plataforma MeData. Estos datos son abiertos al público. Se presentará la visualización en un mapa de accidentalidad por tipo de accidente.

# Problemática
Exponer bajo diferentes grados de accidentalidad el peligro en las vías en la ciudad de Medellín. Con base en esto se puede observar cuáles son las cualidades que se repiten en las calles más peligrosas de la ciudad. Así, se podría buscar mejorar la seguridad vial en Medellín, haciéndola una ciudad para todos. 

# Procedimiento
1. Inicialmente, se eliminarion los siguientes campos:

   * CBML = No relevante para el análisis.
   * DIRECCION = Se tiene la variable de location.
   * DIRECCION ENCASILLADA = Se repite.
   * EXPEDIENTE = Es un registro aleatorio sin análisis.
   * FECHA_ACCIDENTES = Se repite.
   * NRO_RADICADO = Numero aleatorio.
   * COMUNA = se tumba comuna pues tiene mucho nan y existe otra columna con la misma información
   * X & Y = Debido a que ya tenemos una columna de localización

2. Se solucionan problemas de encoding. Usando la función .unique() de python, se puede ver que hay datos con fallas debido a caracteres especiales, como tildes o la 'ñ', que no pertenece al teclado anglosajón. Por ejemplo, varias tildes fueron reemplazadas por códigos. Por lo tanto, en la variable DISEÑO, antes de corregirlo vemos 'Pont\\xF3n' en vez de 'Pontón'.

Para el número de comuna hay datos que no son consistentes ('Sin Inf','In','SN','0','AU'). Se coloca NA ya que no tenemos información de esta.

3. No se puede convertir a formato fecha de la siguiente forma "df["FECHA_ACCIDENTE"]=pd.to_datetime(df["FECHA_ACCIDENTE"],format="%d/%m/%Y %H:%M:%S")" ya que hay campos que no cumplen el formato como por ejemplo '13/05/2016 Sin Inf'. Pero creamos nuevas variables HORA , FECHA, SEMANA, MES, DIA DEL AÑO, DIA DEL MES, DIA DE LA SEMANA.

4. De la variable 'LOCATION' generamos 'LOCATION 2' y de esta última nuevas variables para la longitud y la altitud para ubicar en el mapa los accidentes.

5. De la variable 'HORA' generamos 'MOMENTO', que discrimina los horarios del accidente cada 6 horas por "Mañana", "Tarde", "Noche" y "Madrugada".

6. Se analizan los datos null. Se inspecciona que cantidad de datos se consideran perdidos y/o incompletos. Los resultados discretizados por mes y año se pueden observar en la figura 1:

<img src="/Graficas/data_perdida.png" alt="data_perdida" title="Data perdida">

*figura 1: Data completa y data perdida.*

7. Se elabora una gráfica para observar los meses con mayor accidentalidad (o con mayor cantidad de datos recogidos). Se observa en la figura 2 que agosto es el mes con mayor cantidad de accidentalidad. Y que en general, hay menos accidentes en la primera mitad del año que en el segundo semestre. 

<img src="/Graficas/incidentalidad_mes.png" alt="accidentalidad_mes" title="accidentalidad mes">
*figura 2: accidentalidad por mes*

8. Se eliminan los datos con data perdida dado que son menores en cantidad. 

9. Se le hace un descriptivo a los datos. Se puede observar en la tabla 1 la cantidad por clase de accidente y en la segunda, la cantidad de accidentes según su gravedad. 

  | Clase de accidente | Cantidad |
  | --- | --- |
  |Choque| 168510 |
  |Otro| 26653 |
  |Atropello| 23419|
  |Caída de ocupante| 21453 |
  |Volcamiento| 9020 |
  |Incendio| 28 |
*tabla 1: clase de accidente*

  |Gravedad | Cantidad |
  | --- | --- |
  |Con heridos| 136916 |
  |Solo daños| 111845 |
  |Con muertos| 322 |
  
  *tabla 2: gravedad del accidente*
   
También se observó una caída en la accidentalidad en Medellín en 2020 debido a la pandemia del Covid-19. Esto se puede observar en la figura 3. 
   
   <img src="/Graficas/frecuencias.png" alt="frecuencias" title="frecuencias">
   
*figura 3: frecuencias*

10. Se separan las bases por tipo de accidente. 
11. Se hace el modelo para los choques. Se le hace el one hot enconding y pycaret.regression para hallar múltiples modelos utilizando diferentes métodos estocásticos de modelo. Nos quedamos con el modelo gbr ("Gradient boosting regressor"). Finalmente se calcula el error cuadrático medio RMSE. Se repite un modelo similar para los atropellos, donde se elige un modelo br ("Bayesian ridge"); caida, donde se usa un modelo ridge ("ridge regression"); volcamiento, donde se usa un modelo omp ("Orthogonal matchin pursuit"); otro, donde también se usa br; incendio, que no se le asigna ningún modelo.   
12. Se agrupan los datos por el nombre de su barrio, guardando el total de sus accidentes con heridos, solo con daños o con muertos. Quedan los datos de 340 barrios (o áreas, como las áreas de expansión de altavista). 
13. Se normalizan los datos ordenados por barrio. Se utiliza el método MinMax. 
14. Se realiza un dendograma, que se puede observar en la figura 4. 
  <img src="/Graficas/dendo.png" alt="dendograma" title="dendograma">
  
*figura 4: dendograma*

Se observan grandes diferencias en un conjunto pequeño de datos (el que se ve de color verde, hacia la izquierda).

15. Se realiza una gráfica de la curva Elbow para decidir el número n de clusters. Como se puede observar en la figura 5, por el cambio en la gráfica, se opta por utilizar 3 clusters. 

<img src="/Graficas/elbow.png" alt="elbow" title="elbow">

*figura 5: curva de elbow*

## Caracterización
### Cluster 0
Es el que tiene una mayor cantidad de barrios, con 245 de estos. 
Se puede observar en su cantidad de Accidentes - Heridos - Daños - Muertos que representan los barrios con menor accidentalidad. Su cantidad de accidentes, heridos y daños son los menores entre los 3 cluster. 

### Cluster 1
Tiene 72 barrios. 
Tiene una incidencia intermedia de accidentes, donde se aumentan tanto los accidentes como los heridos y los daños.

### Cluster 3
Es el clúster con menor número de barrios, con un total de 23. 
Siendo así, cada uno de estos barrios se caracteriza por tener la mayor cantidad de accidentes, y, al mismo tiempo, son los accidentes más peligrosos, es decir, con más heridos y más incidencia en muertes.

# Variables
	 	 	  	  	 	  	  	

 |Gravedad | Cantidad |
  | --- | --- |
  |AÑO | Año en que sucedió el accidente/incidente |
  |CLASE_ACCIDENTE | Tipo de accidente |
  |DISEÑO | Tipo de vía en la que sucedió |
  |GRAVEDAD_ACCIDENTE | Expone si hubo heridos/muertos |
  |MES | Número del 1 al 12 que indica el mes |
  |NUMCOMUNA | Número de la comuna de Medellín |
  |BARRIO | Nombre del barrio de Medellín |
  |LONGITUD | Longitud en grados del accidente |
  |LATITUD | Latitud en grados del accidente |
  |MOMENTO | Momento del día según la hora del accidente |
  |SEMANA | Número de la semana en que ocurrió el accidente |
  
*tabla 3: Leyenda Mapa*
  

# Mapa de Medellín

  |Color | Cluster | Caracterización |
  | --- | --- | --- |
  |Rojo | 2 | Alto riesgo de accidentes y peligro. Peligro alto | 
  |Morado | 1 | Peligro moderado. Peligro Medio |
  |Azul | 0 | Peligro bajo|
  
*tabla 4: Leyenda Mapa*
  
  #MAPA MEDELLIN POR FAVOR AAAAAAAAAAAAA

# Conclusiones
* La mayoría de barrios peligrosos van ligados a la autopista Regional y a la autopista Norte y sus alrededores. Esto se debe a que son vías en las que se conduce a una mayor velocidad. Además, se observa que la mayoría de barrios que quedan en la zona de las autopistas en la comuna 10 - La Candelaria, representan un gran riesgo. En esta zona, se suma una mayor velocidad en las vías con una densidad poblacional muy alta, con cruce constante de personas. 
* De manera similar, los barrios del cluster 1, es decir, los de intermedia incidentalidad, suelen estar cerca a vías de alta concurrencia diferentes a las autopistas, tales como San Juan, la calle 33 y la 30, la avenida el Poblado (la carrera 43a), entre otras. 
* La mayoría de barrios de cuadras pequeñas pertenecen al cluster 0, teniendo la menor accidentalidad. Esto, en parte, se podría deber a que, al tener cuadras más pequeñas, los carros se ven obligados a conducir más lento, por lo que la mayoría de choques serían incidentes y no accidentes. Por otro lado, es claro que en una vía en la que transcurren muchos más carros, como la que lleva de un lado a otro de la ciudad, exista una mayor probabilidad de que haya un accidente. 

# Bibliografía
* [1] "Hadoop Integration" (2021, Marzo 6). Incidentes viales  [Online]. Available: http://medata.gov.co/dataset/incidentes-viales
* [2] "MEData" (SF). El portal de datos de Medellín  [Online]. Available: http://medata.gov.co/
* [3] "MinTIC" (SF). Ministerio de tecnologías de la información y las comunicaciones [Online]. Available:https://www.mintic.gov.co/portal/inicio/
* [4] "Secretaría de movilidad" (SF). Secretaría de movilidad de Medellín [Online]. Available: https://www.medellin.gov.co/movilidad/
