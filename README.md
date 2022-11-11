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

_figura 1: Data completa y data perdida. _

7. Se elabora una gráfica para observar los meses con mayor accidentalidad (o con mayor cantidad de datos recogidos). Se observa en la figura 2 que agosto es el mes con mayor cantidad de accidentalidad. Y que en general, hay menos accidentes en la primera mitad del año que en el segundo semestre. 

<img src="/Graficas/incidentalidad_mes.png" alt="accidentalidad_mes" title="accidentalidad mes">
_figura 2: accidentalidad por mes. _

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
  
  *tabla 1: clase de accidente.*

|Gravedad | Cantidad |
  | --- | --- |
  |Con heridos| 136916 |
  |Solo daños| 111845 |
  |Con muertos| 322 |
   
   *tabla 2: gravedad del accidente.*
   
También se observó una caída en la accidentalidad en Medellín en 2020 debido a la pandemia del Covid-19. Esto se puede observar en la figura 3. 
   
   <img src="/Graficas/frecuencias.png" alt="frecuencias" title="frecuencias">
*figura 3: frecuencias.*

10. Se separan las bases por tipo de accidente. 
11. Se hace el modelo para los choques. Se le hace el one hot enconding y pycaret.regression para hallar múltiples modelos utilizando diferentes métodos estocásticos de modelo. Nos quedamos con el modelo gbr ("Gradient boosting regressor"). Finalmente se calcula el error cuadrático medio RMSE. Se repite un modelo similar para los atropellos, donde se elige un modelo br ("Bayesian ridge"); caida, donde se usa un modelo ridge ("ridge regression"); volcamiento, donde se usa un modelo omp ("Orthogonal matchin pursuit"); otro, donde también se usa br; incendio, que no se le asigna ningún modelo.   
12. Se agrupan los datos por el nombre de su barrio, guardando el total de sus accidentes con heridos, solo con daños o con muertos. Quedan los datos de 340 barrios (o áreas, como las áreas de expansión de altavista). 
13. Se normalizan los datos ordenados por barrio. Se utiliza el método MinMax. 
14. Se realiza un dendograma, que se puede observar en la figura 4. 
  <img src="/Graficas/dendo.png" alt="dendograma" title="dendograma">
*figura 4: dendograma.*

Se observan grandes diferencias en un conjunto pequeño de datos (el que se ve de color verde, hacia la izquierda).



# Variables

# Análisis de las variables seleccionadas

# Conclusiones

# Bibliografía
