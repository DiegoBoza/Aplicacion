import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# Propuesta de aplicación
##### Se realizo una encuesta a 33 personas sobre el nivel de satisfacción de películas y series

#### El tema de nuestra encuentas fue:  PELICULAS

Donde para contestar a las preguntas que se planteaba era mediante la escala de likert, el cual consiste en:

**1 (Nada satisfecho)**

**2 (Poco satisfecho)**

**3 (Neutral)**

**4 (Muy satisfecho)**

**5 (Totalmente satisfecho)**

### Formulario de Google (Preguntas)
""")
from PIL import Image
image = Image.open('encuesta.png')

st.image(image, caption='')

st.write("""
#### Formulario de Google (Imagenes)
""")
from PIL import Image
image = Image.open('encuesta2.png')

st.image(image, caption='')

st.write("""
#### Formulario de Google (Preprocesamiento)
""")
from PIL import Image
image = Image.open('encuesta3.png')

st.image(image, caption='')

st.write("""
## Resultados de la encuesta
# """)

#Importamos librerias para Ciencia de Datos y Machine Learning
import math
import numpy as np
import pandas as pd

#archivo CSV separado por comas
data = pd.read_csv('Peliculas.csv', engine ='python')

#leer  lineas
data

