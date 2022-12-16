import streamlit as st
import pandas as pd
import numpy as np

st.write(""" 
# Anális de Correlación
El **análisis de correlación** es el primer paso para construir modelos explicativos y predictivos más complejos.

A menudo nos interesa observar y medir la relación entre 2 variables numéricas mediante el análisis de correlación. 
Se trata de una de las *técnicas más habituales en análisis de datos* y el primer paso necesario antes de construir cualquier modelo explicativo o predictivo más complejo
Para poder tener el  Datset hay que recolectar información a travez de encuentas.
""")

st.write("""
## ¿Qué es la correlación?

El análisis de correlación implica un procedimiento estadístico para determinar si dos variables están relacionadas. El resultado del análisis es un coeficiente de correlación, cuyos valores pueden estar entre -1 y 1.

El símbolo indica el tipo de correlación entre dos variables. Un signo positivo indica una relación positiva entre dos variables; es decir, a medida que aumenta el tamaño de uno, también lo hace el otro. Un signo negativo indica que existe una relación negativa entre las dos variables. A medida que aumenta el valor de una variable, disminuye el valor de la otra variable. Si dos variables son independientes, la magnitud del coeficiente de correlación es cero.

La fuerza de la relación lineal aumenta a medida que el coeficiente de correlación se aproxima a -1 o 1. 
El análisis de correlación es un enfoque estadístico que se utiliza para determinar la relación entre las variables cuantitativas o categóricas.

Cuando quieres determinar la correlación a través del análisis de datos, hay dos tipos de información con la que debes trabajar:

**- Datos univariados:** Cuando quieres trabajar con una sola variable, es necesario medir la tendencia central a preguntar por los datos representativos y conocer su desviación a través de la dispersión, medir la forma y el tamaño de la distribución a través de la asimetría y medir la concentración de datos en la posición central a través de la curtosis. Por lo tanto, los datos relativos a una sola variable se denominan datos univariados.

**- Datos bivariados:** El análisis de correlación se trata más bien de estudiar la relación entre dos variables al mismo tiempo.Por ejemplo, el precio de un producto y sus ventas medias, o la edad y la presión arterial de una persona. Así, dos caracteres de la misma entidad cuando se miden simultáneamente con la ayuda de un análisis estadístico, los denominamos datos bivariados.
La correlación es en esencia una medida normalizada de asociación o covariación lineal entre dos variables. Esta medida o índice de correlación r puede variar entre -1 y +1, ambos extremos indicando correlaciones perfectas, negativa y positiva respectivamente. Un valor de r = 0 indica que no existe relación lineal entre las dos variables. Una correlación positiva indica que ambas variables varían en el mismo sentido. Una correlación negativa significa que ambas variables varían en sentidos opuestos. Lo interesante del índice de correlación es que r es en sí mismo una medida del tamaño del efecto, que suele interpretarse de la siguiente manera:


**- correlación despreciable: r < |0.1|**

**- correlación baja: |0.1| < r <= |0.3|**

**- correlación mediana : |0.3| < r <= |0.5|**

**-correlación fuerte o alta: r > |0.5|**
""")
from PIL import Image
image = Image.open('descarga.png')

st.image(image, caption='')

st.write("""
## Definiciones formales 
La correlación se define en términos de la varianza (s²) de las variables x e y, así como de la covarianza cov de x,y. Es por tanto una medida de la variación conjunta de ambas variables (cov(x,y)).

## Varianza (s²)
La varianza de una muestra representa el promedio de la desviación de los datos con respecto a la media.
""")
from PIL import Image
image = Image.open('formula.png')

st.image(image, caption='')

st.write("""
## Covarianza cov(x,y)
La covarianza entre dos variables x e y es una medida de la relación “promedio” éstas. Es la desviación promedio del producto cruzado entre ellas:
""")
from PIL import Image
image = Image.open('formula2.png')
st.image(image, caption='')

st.write("""
Veamos un ejemplo de dos variables que co-varían (respuesta ~ dosis en 5 pacientes), es decir, que están correlacionadas.
Los datos: dosis=(8,9,10,13,15); resp=(5,4,4,6,8);""")

from PIL import Image
image = Image.open('cuadro.png')
st.image(image, caption='')

st.write("""
# Tipos de análisis de correlación

Si hay algún tipo de correlación entre dos variables, ambas se alteran juntas durante un período de tiempo. La correlación encontrada puede ser positiva o negativa, dependiendo de los valores numéricos medidos.

**Análisis de correlación positiva:** Cuando debido a un aumento en cualquiera de las variables, la otra variable también comienza a aumentar asegurando una correlación positiva entre ellas. 

**Análisis de correlación negativa:** Cuando debido al aumento en cualquiera de las variables, la otra variable comienza a disminuir asegurando una correlación negativa entre ellas.

""")
from PIL import Image
image = Image.open('grafico1.png')
st.image(image, caption='')

st.write("""
## ¿Cómo se mide la correlación?
La fórmula general para calcular el coeficiente de correlación entre dos variables es:
""")
from PIL import Image
image = Image.open('grafico2.png')
st.image(image, caption='')

st.write("""
El coeficiente de correlación es el resultado de dividir la covarianza entre las variables X y Y entre la raíz cuadrada del producto de la varianza de X y la de Y.

**1. Calcular la covarianza entre la variable X y la variable Y (entre las dos columnas de la matriz) de acuerdo a la siguiente fórmula:**

""")
from PIL import Image
image = Image.open('grafico2.png')
st.image(image, caption='')

st.write("""
Se calcula la media de todos los valores de X y de Y Se realiza la sumatoria del producto de las diferencias entre cada observación de cada variable y su media correspondiente. La sumatoria calculada anteriormente se divide entre el número total de observaciones menos 1.

**2. Calcular las varianza de la variable X y la varianza de la variable Y y obtener la raíz cuadrada de cada una:**
""")
from PIL import Image
image = Image.open('grafico3.png')
st.image(image, caption='')

st.write("""
Para cada variable se calcula la desviación estándar y se multiplican

**3. Se divide la covarianza entre el producto de las desviaciones estándar**

Ejemplo en R:

**1. Crear dos variables dependientes**

**2. Utilizar la función cor() O utilizar la fórmula antes propuesta**

## Métodos para realizar un análisis de correlación

En los métodos estadísticos, el coeficiente de correlación “r” mide la fuerza, dirección y extensión de la relación entre dos variables, donde el valor de “r” siempre oscilará entre +1 y -1. 

Recuerda, es inútil calcular la correlación si no hay relación entre las dos variables, ya que la correlación sólo se aplica a las relaciones lineales. Por el contrario, si existe una fuerte relación entre las dos variables, pero no es lineal, la correlación recibida puede ser engañosa. 

Es aconsejable que antes de llevar a cabo una investigación de correlación utilizando cualquiera de los métodos, examines primero el diagrama de dispersión. 

A continuación, se presentan algunos de los métodos de correlación de coeficientes más utilizados.

## - Método del diagrama de dispersión

La relación entre las dos variables se presenta en forma de diagrama para comprender cuán estrechamente se relacionan entre sí.

**- También, llamada gráfica de dispersión o tabla de correlación.**

**- El diagrama o el gráfico tiene dos variables a lo largo de sus ejes `x’ y `y’, de las cuales una es independiente y la otra es la variable dependiente.**

**- Es fácil predecir el comportamiento de la variable independiente dependiendo de la medida de su medida.**

**- Según el tipo de correlación, los diagramas de dispersión se dividen en diagramas de dispersión sin correlación, diagramas de dispersión con correlación moderada y diagramas de dispersión con una fuerte correlación.**

""")
from PIL import Image
image = Image.open('grafico4.jpg')
st.image(image, caption='')

st.write("""
## - Coeficiente de Spearman

Es una versión no paramétrica de la correlación del coeficiente de Pearson. Este método se utiliza para medir la fuerza y dirección de la relación o asociación existente entre las dos variables.

**- La letra griega “ρ” se utiliza para indicar el Coeficiente de Correlación de Spearman.**

**- También se indica con el símbolo rs.**

**- Spearman se utiliza tanto para variables ordinales como para datos continuos que han fallado en las suposiciones necesarias para llevar a cabo el coeficiente de correlación de Pearson.**

Fórmula de coeficiente de Spearman:
""")
from PIL import Image
image = Image.open('grafico6.jpg')
st.image(image, caption='')

st.write("""
## - Metodo de Pearson

El coeficiente de correlación de Pearson es una prueba que mide la relación estadística entre dos variables continuas. Si la asociación entre los elementos no es lineal, entonces el coeficiente no se encuentra representado adecuadamente.

El coeficiente de correlación puede tomar un rango de valores de +1 a -1. Un valor de 0 indica que no hay asociación entre las dos variables. Un valor mayor que 0 indica una asociación positiva. Es decir, a medida que aumenta el valor de una variable, también lo hace el valor de la otra. Un valor menor que 0 indica una asociación negativa; es decir, a medida que aumenta el valor de una variable, el valor de la otra disminuye.

Para llevar a cabo la correlación de Pearson es necesario cumplir lo siguiente:

**- La escala de medida debe ser una escala de intervalo o relación.**

**- Las variables deben estar distribuida de forma aproximada.**

**- La asociación debe ser lineal.**

**- No debe haber valores atípicos en los datos.**

### Cómo se calcula el coeficiente de correlación de Pearson

La fórmula del coeficiente de correlación de Pearson es la siguiente:

""")

from PIL import Image
image = Image.open('grafico6.png')
st.image(image, caption='')

st.write("""
Donde:

“x” es igual a la variable número uno, “y” pertenece a la variable número dos, “zx” es la desviación estándar de la variable uno, “zy” es la desviación estándar de la variable dos y “N” es es número de datos.

### Interpretación del coeficiente de correlación de Karl Pearson

El coeficiente de correlación de Pearson tiene el objetivo de indicar cuán asociadas se encuentran dos variables entre sí por lo que:

""")

st.write("""
## - Método de los mínimos cuadrados
Es un problema matemático que se utiliza para encontrar el grado de correlación entre las dos variables utilizando la raíz cuadrada del producto de dos coeficientes de regresión, el de “x” en “y” o el de “y” en “x”. 

**- El método del cuadrado mínimo asegura que el total del cuadrado de los errores sea lo más bajo posible.**

**- También se conoce como la “Línea de Mejor Ajuste”**

**- Se utiliza para calcular la media de los valores "x" e "y".**

Fórmula del método de los mínimos cuadrados:

""")

from PIL import Image
image = Image.open('grafico7.png')
st.image(image, caption='')

st.write("""
**Correlación menor a cero:** Si la correlación es menor a cero, significa que es negativa, es decir, que las variables se relacionan inversamente.

Cuando el valor de alguna variable es alto, el valor de la otra variable es bajo. Mientras más próximo se encuentre a -1, más clara será la covariación extrema. Si el coeficiente es igual a -1, nos referimos a una correlación negativa perfecta.

**Correlación mayor a cero:** Si la correlación es igual a +1 significa que es positiva perfecta. En este caso significa que la correlación es positiva, es decir, que las variables se correlacionan directamente.

Cuando el valor de una variable es alto, el valor de la otra también lo es, sucede lo mismo cuando son bajos. Si es cercano a +1, el coeficiente será la covariación.

**Correlación igual a cero:** Cuando la correlación es igual a cero significa que no es posible determinar algún sentido de covariación. Sin embargo, no significa que no exista una relación no lineal entre las variables.

Cuando las variables son independientes significa que estas se encuentra correlacionadas, pero esto nos significa que el resultado sea verdadero.

""")
from PIL import Image
image = Image.open('grafico8.png')
st.image(image, caption='')

from PIL import Image
image = Image.open('grafico9.png')
st.image(image, caption='')

st.write("""
### Ventajas y desventajas del coeficiente de correlación de Pearson

Entre las principales ventajas del coeficiente de correlación de Karl Pearson se encuentran:

**- El valor es independiente de cualquier unidad que se utiliza para medir las variables.**

**- Si la muestra es grande, es más probable la exactitud de la estimación.**

Alguna de las desventajas del coeficiente de correlación son:

**- Es necesario las dos variables sean medidas a un nivel cuantitativo continuo.**

**- La distribución de las variables deben ser semejantes a la curva normal.**

## ¿Qué es la escala de Likert?

La Escala de Likert es una escala de calificación que se utiliza para cuestionar a una persona sobre su nivel de acuerdo o desacuerdo con una declaración. Es ideal para medir reacciones, actitudes y comportamientos de una persona.

A diferencia de una simple pregunta de “sí” / “no”, la escala de Likert permite a los encuestados calificar sus respuestas.

Se le da este nombre por el psicólogo Rensis Likert. Likert distinguió entre una escala apropiada, la cual emerge de las respuestas colectivas a un grupo de ítems (pueden ser 8 o más), y el formato en el cual las respuestas son puntuadas en un rango de valores.

Técnicamente, una escala de likert hace referencia al último. La diferencia de estos dos conceptos tiene que ver con la distinción que Likert hizo entre el fenómeno que está siendo investigado y las variables de los medios de captura.

La escala de Likert es uno de los tipos de escalas de medición utilizados principalmente en la investigación de mercados para la comprensión de las opiniones y actitudes de un consumidor hacia una marca, producto o mercado meta. Nos sirve principalmente para realizar mediciones y conocer sobre el grado de conformidad de una persona o encuestado hacia determinada oración afirmativa o negativa.

Cuando se responde a un ítem de la escala de likert, el usuario responde específicamente en base a su nivel de acuerdo o desacuerdo. Las escalas de frecuencia con la de Likert utilizan formato de respuestas fijos que son utilizados para medir actitudes y opiniones. Estas escalas permiten determinar el nivel de acuerdo o desacuerdo de los encuestados.

La escala de Likert asume que la fuerza e intensidad de la experiencia es lineal, por lo tanto va desde un totalmente de acuerdo a un totalmente desacuerdo, asumiendo que las actitudes pueden ser medidas.

Las respuestas pueden ser ofrecidas en diferentes niveles de medición, permitiendo escalas de 5, 7 y 9 elementos configurados previamente. Siempre se debe tener un elemento neutral para aquellos usuarios que ni de acuerdo ni en desacuerdo.


""")

from PIL import Image
image = Image.open('grafico7.jpg')
st.image(image, caption='')

st.write("""
## ¿Cómo hacer una escala de Likert?

A continuación te presentaremos algunas recomendaciones para crear una pregunta con escala de Likert:

**2. Mantén la coherencia de los adjetivos:**
Presta mucha atención al uso de adjetivos en las preguntas tipo Likert para asegurarte de que los encuestados puedan entender claramente el significado de cada opción. Cada adjetivo debe tener una posición clara en la escala, de mayor a menor. 

Utiliza el término “extremadamente” para los dos extremos de la escala (por ejemplo, “muy de acuerdo” “muy en desacuerdo”), establece un punto medio neutral (por ejemplo, “ni de acuerdo ni en desacuerdo”) y completa las valoraciones moderadas con los mismos adjetivos (por ejemplo, “algo en desacuerdo”, “algo de acuerdo”).

**3. Considera la escala unipolar y la bipolar:**
Las escalas Likert son bipolares o unipolares, es decir, tienen dos extremos o uno. 

Utiliza escalas bipolares cuando desees que los encuestados respondan en un lado positivo o negativo de la neutralidad. Por ejemplo, la pregunta “¿Con qué probabilidad recomendarías este producto?” iría de “Muy poco probable” a “Muy probable”, con “Indeciso” como punto medio.

Las escalas unipolares operan desde una escala de cero a una extrema. Por ejemplo, la pregunta “¿Qué tan bueno le parece este producto?” podría tener opciones que van desde “Nada bueno” hasta “Extremadamente bueno”.

**4. Selecciona los ítems cuidadosamente:**
Los ítems se deben relacionar fácilmente con las respuestas de la oración, sin importar que la relación entre ítem y oración sea evidente.

Los ítems deben de tener siempre dos posturas extremas así como un ítem intermedio que sirva de graduación entre los extremos. Es importante mencionar que a pesar de que la escala de Likert más común es la de 5 ítems, el uso de más ítems ayuda a generar mayor precisión en los resultados.

Los ítems de la escala deben ser siempre seguros y fiables. Para lograr la fiabilidad en ocasiones es necesario sacrificar la precisión de la escala.

""")

from PIL import Image
image = Image.open('images.jpeg')
st.image(image, caption='')

st.write("""
## Ventajas y desventajas de usar la escala de likert

Considera los siguientes puntos antes de aplicar la escala de likert y decide si es el tipo de pregunta que debes usar para la recolección de datos de tu próximo proyecto de investigación.

**- Es una escala de fácil aplicación y diseño.**

**- Puede utilizar ítems que no tienen relación con la expresión.**

**- Ofrece una graduación de la opinión de las personas encuestadas.**

**- Produce mediciones de calidad (precisas y que minimizan el error de medición)**

**- Permite realizar los análisis necesarios para alcanzar los objetivos de la investigación.**

**- Se pueden hacer comparaciones con evaluaciones anteriores del servicio o con servicios similares (benchmarking).**

**- Muy sencilla de contestar.**

## Desventajas de una escala de likert

**- Existen estudios científicos que indican que existe un sesgo en la escala, ya que las respuestas positivas siempre superan a las negativas.**

**- También hay estudios que indican que los encuestados tienden a contestar “de acuerdo” ya que implica un menor esfuerzo mental a la hora de contestar la encuesta.**

**- Dificultad para establecer con precisión la cantidad de respuestas positivas y negativas.**

**- Si te ha quedado claro todo, es momento de crear tu primera encuesta online utilizando la escala de Likert.**
""")
