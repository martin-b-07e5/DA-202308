# DA-202308 - main

url: [https://campiasjuan.notion.site/campiasjuan/Trabajo-Final-c499b5392e9c4001b4ef7a9d28ad6935](https://www.notion.so/Trabajo-Final-c499b5392e9c4001b4ef7a9d28ad6935?pvs=21)

## Objetivo 👈

- Crear un proyecto que consuma datos
- podrás seleccionar 3 fuentes distintas para popular una base de datos SQL, con la información contenida en la Response de nuestro script de Python.

## Requerimientos funcionales 🔎

1. los archivos fuente
2. el procesamiento de datos
3. la creación de tablas en la base de datos
4. la actualización de la base de datos.
Veamos cada uno de ellos en detalle.

## Archivos fuente:

- Los archivos fuentes serán utilizados en tu proyecto para obtener de ellos todo lo
necesario para popular la base de datos.

---
---
---

# El proyecto deberá:


## ✅Nivel inicial:

1. ✅Obtener el archivo de la fuente que escojamos,
    1. ✅Archivos de fuente utilizando Google Colab y la librería requests
2. ✅Almacenarse en forma local en formato CSV:

### ✅Librerias necesarias:

```python
from datetime import datetime
import requests
import pandas as pd
from pandas import json_normalize
import json
```

### ✅API de datos abiertos del clima:

API: https://openweathermap.org/api

1. ✅Realizar una solicitud HTTP a la API para obtener los datos en formato JSON y luego convertirlos a CSV utilizando Python.

BASE_URL = "'https://api.openweathermap.org/data/2.5/weather["](https://api.openweathermap.org/data/2.5/onecall/timemachine?%22)

1. ✅Organizar los archivos en rutas siguiendo la siguiente estructura:
“data_analytics\openweather\tiempodiario_yyyymmdd.csv”
La fecha de la nomenclatura es la fecha del tiempo tomado.
2. ✅buscar estas ciudades:

```python
cityList = ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico DF", "Dublin", "Tilfis", "Bogota", "Tokio"]
coordList = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58", "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]
```

1. ✅Realizar los comentarios correspondientes para una correcta comprensión del código. (#)

---
---
---

# 👷Nivel medio:

1. ✅La descarga, procesamiento y actualización de la información en la **base de datos**
se debe poder ejecutar desde un archivo .py
2. 👷El proyecto debe poder deployarse en forma sencilla siguiendo un **readme,** que al menos contenga las **instrucciones** para:
    1.  Utilizarse creando un entorno virtual (venv)
    2. Instalar las dependencias necesarias con pip.
    3. Configurar la conexión a la base de datos.

### Enpoint:

BASE_URL = "[https://api.openweathermap.org/data/2.5/onecall/timemachine?"](https://api.openweathermap.org/data/2.5/onecall/timemachine?%22)

### Documentación

💡onecall/timemachine
https://openweathermap.org/api/one-call-api#history-how



✅**Tomar 5 días de cada ciudad.**

1. Normalizar Tabla teniendo en cuenta el formato y el tipo de dato contenido en cada columna.
2. Las configuraciones necesarias para que el proyecto se ejecute deben poder, configurarse desde un archivo config.py
3. Realizar los comentarios correspondientes para su correcta documentación con docstrings(’’’ ‘’’).

---
---
---
## Bases de datos

1. Se deben dejar disponibles los scripts de creación de las tablas utilizadas.
2. Conexión a la base de datos:
    1. Los datos se deben almacenar en una base PostgreSQL.
    2. La conexión a la base de datos se debe implementar con la librería y ORM **SQLalchemy**.
    3. Se recomienda ver la funcionalidad de pandas dataframe.to_sql.

## ****Herramientas para el procesamiento de datos:****

Utilizar la librería Pandas para procesar los datos obtenidos y almacenarlos en la base de datos PostgreSQL.

**Explicación:**

1. La librería Pandas se utilizará para leer los datos en formato CSV y procesarlos antes de cargarlos en la base de datos.

**Parte Práctica:**
Ya hemos utilizado la librería Pandas en la parte práctica anterior, donde hemos procesado los datos y los hemos cargado en la base de datos utilizando esta herramienta.

---