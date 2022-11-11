# Trabajo 2 de Técnicas en Aprendizaje Estadístico de la UNAL-med 

## A cargo de:

- Esteban García Carmona
- Emilio Porras Mejía
- Felipe Miranda Arboleda
- José Luis Suárez Ledesma

## Introducción 
En el presente informe se buscará tratar de predecir la accidentalidad en la ciudad de Medellín con base en la información de accidentes reportados a través de la plataforma MeData. Estos datos son abiertos al público. Se presentará la visualización en un mapa de accidentalidad por tipo de accidente.

# Problemática
Exponer bajo diferentes grados de incidentalidad el peligro en las vías en la ciudad de Medellín. Con base en esto se puede observar cuáles son las cualidades que se repiten en las calles más peligrosas de la ciudad. Así, se podría buscar mejorar la seguridad vial en Medellín, haciéndola una ciudad para todos. 

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

####figura 1

_figura 1


# Variables

# Análisis de las variables seleccionadas

# Conclusiones

# Bibliografía
