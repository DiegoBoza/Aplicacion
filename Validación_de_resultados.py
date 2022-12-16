import streamlit as st
import pandas as pd
import numpy as np
import math


st.write("""
# Validación de resultados
 importamos el archivo""")
# archivo CSV separado por comas
data = pd.read_csv('Peliculas.csv', engine='python')

#leer  lineas
data

# Numero de encuestados y numero de preguntas - 1
data.shape

st.write("""
Como se puede observa se genera unos elementos llamados <NA>, estos representan respuestas vacias en el formulario.

Estos seran reemplazados por la mediana de cada columna, quedando asi:
""")
# Tipos de datos
data.dtypes

st.write("""
# Resultados sin NaNs""")

# cantidad de NaNs po columna
data.isnull().sum()

#Calculamos la mediana de cada columna
data.median(numeric_only=True)

#Reemplazo los datos con la mediana

valores = data.fillna(data.median(numeric_only=True))
valores

preferencias = valores[valores.columns[1:]].to_numpy()   #n
encuestados = valores[valores.columns[0]].to_numpy()   #m
print(preferencias)
print(encuestados)

st.write("""
# Correlacion de pearson con datos limpios""")
preferencias.T


# Establecemos nuevas variables para trabajar
nae = valores[valores.columns[1:]].to_numpy()
moe = valores[valores.columns[0]].to_numpy()

# Generamos la "matriz" de correlación de preferencias y encuestados
matriz = pd.DataFrame(preferencias.T, columns = encuestados)
# Creamos una función que ejecute la fórmula de pearson

lista = []
#Describimos todas las operaciones de la fórmula de pearson
def matrix_de_correlacion(x,y):
    media_x = x.mean()     #Establecemos la media de x
    media_y = y.mean()     #Establecemos la media de y
    diferencia_x = x - media_x  #Establecemos la diferencia de las x
    diferencia_y = y - media_y  #Establecemos la diferencia de las y
    suma_numerador = np.sum((x - media_x)*(y - media_y)) #suma del numerador
    suma_p1 = np.sum((diferencia_x)**2)  #Primera suma (x) del denominador
    suma_p2 = np.sum((diferencia_y)**2)  #Segunda suma (x) del denominador
    primera_raiz = np.sqrt(suma_p1)    #Primera raiz del numerador
    segunda_raiz = np.sqrt(suma_p2)    #Segunda raiz del numerador
    
    coeficiente_r = suma_numerador/((primera_raiz)*(segunda_raiz))
    return coeficiente_r

#Aplicamos un for para recorrer todos los datos

for i in range(len(moe)):
    for j in range(len(moe)):
        a = valores.loc[[i,j],:]
        b =a[a.columns[1:]].to_numpy()
        lista.append(matrix_de_correlacion(b[0],b[1]))

st.write("""
# Correlacion en Array """)

#Convertimos los datos en un cuadro
cuadro = np.array(lista).reshape(len(moe),len(moe))
cuadro

st.write("""
# Matrix de correlación """)

cuadro2 = pd.read_csv('Encuestados.csv', engine='python')

#leer  lineas
cuadro2

("""
# Gráfica de calor """)

from PIL import Image
image = Image.open('calor.png')
st.image(image, caption='')

st.write("""
# Grafico extra """)

import pandas as pd
import numpy as np

chart_data = pd.DataFrame(preferencias.T, columns = encuestados)

st.line_chart(chart_data)

st.write("""
# Conclusiones 
###  ¿Se valido o no los resultados?

   - Efectivamente, los resultados obtenidos fueron validados en ambos metodos, dandonos el mismo resultado.

### Los resultados validados son:

 1. **"luisitotomoki40"** y  **"yeyogou478"**  obtienen el **"PRIMER"** indice mas alto de similitud con: **0.7698** o tambien denotado en porcentaje como **76.98%**
 
 
 2. **"DIEGO ALEXANDER BOZA ANAMPA"** y  **"luisitotomoki40"** obtienen el **"SEGUNDO"** indice mas alto de similitud  con : **0.7384** o tambien denotado en porcentaje como **73.84%**

### ¿Es efectivo el metodo de correlación de pearson?

   - Si, ya que es una medida considerablemente practico además de ser utilizado en diversas áreas del quehacer científico, desde estudios técnicos, econométricos o de ingeniería; hasta investigaciones relacionadas con las ciencias sociales, del comportamiento o de la salud, pero debido a sus varias aplicaciones del metodo de correlación de pearson es que se suele usar de manera inadecuada que incluso afecta a las más experimentados, asi que el metodo de por si, si es efectivo siempre en cuando se use de manera correcta y para lo que se esta midiendo.
   
### Correlación de Pearson y Regresión Lineal, ¿Cuál es su relación?

   - La correlación de pearson cuantifica como de relacionadas están dos variables, mientras que la regresión lineal consiste en generar una ecuación (modelo) que, basándose en la relación existente entre ambas variables, permita predecir el valor de una a partir de la otra.

   - Ambos cuantifican la dirección de una relación entre dos variables.
   
   - Ambos cuantifican la fuerza de una relación entre dos variables.
""")

