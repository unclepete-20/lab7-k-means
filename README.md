# 🧮 K-Means Clustering 🧮

El algoritmo de K-Means es un método de aprendizaje no supervisado utilizado para agrupar datos en clusters o grupos, basado en su similitud.

## 📚 Cómo funciona

K-Means trabaja dividiendo los datos en grupos llamados clusters, de tal manera que los puntos en el mismo cluster sean similares entre sí y diferentes a los puntos en otros clusters. El algoritmo sigue los siguientes pasos:

1. Seleccionar el número K de clusters que se desean obtener.
2. Seleccionar K puntos aleatorios como centros de los clusters.
3. Asignar cada punto de datos al cluster cuyo centro está más cercano.
4. Recalcular los centros de los clusters como el centroide de todos los puntos asignados a ese cluster.
5. Repetir los pasos 3 y 4 hasta que no se produzcan más cambios en la asignación de puntos a clusters.

## 💻 Implementación

El algoritmo de K-Means puede ser implementado en diferentes lenguajes de programación, y existen varias librerías que facilitan su implementación, como scikit-learn en Python. Aquí te dejamos un ejemplo de implementación en Python:

```python
from sklearn.cluster import KMeans
import numpy as np

# Generar datos de ejemplo
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

# Inicializar el modelo de KMeans con 2 clusters
kmeans = KMeans(n_clusters=2)

# Ajustar el modelo a los datos
kmeans.fit(X)

# Obtener las etiquetas de los clusters y los centros
labels = kmeans.labels_
centers = kmeans.cluster_centers_
```
## 🤔 Cuándo utilizar
El algoritmo de K-Means es ampliamente utilizado en diferentes áreas, como análisis de mercado, segmentación de clientes, bioinformática, procesamiento de imágenes, entre otros. Es una buena opción cuando se desea agrupar datos en clusters de manera rápida y sencilla.

## 📈 Ventajas y Desventajas
Algunas de las ventajas del algoritmo de K-Means son:

- Es fácil de implementar y computacionalmente eficiente.
- Es escalable a grandes conjuntos de datos.
- Es útil para encontrar clusters esféricos.

Algunas de las desventajas del algoritmo de K-Means son:

- Requiere que el número de clusters sea especificado de antemano.
- Es sensible a la selección de los centros iniciales.
- No es adecuado para encontrar clusters no esféricos.

## 🌐 Recursos Adicionales

- [Scikit-learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- [K-Means Clustering Algorithm Explained with Examples](https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/)
- [K-Means Clustering Tutorial](https://towardsdatascience.com/k-means-clustering-8e1e64c1561c)

## Investigación sobre PCA

PCA (Principal Component Analysis) es una técnica de análisis de datos utilizada en Machine Learning y estadística para reducir la dimensionalidad de un conjunto de datos. En resumen, PCA busca identificar la estructura subyacente en los datos y representarla con un conjunto más pequeño de variables llamadas componentes principales.

La idea detrás de PCA es encontrar la dirección de máxima variación en los datos y proyectar los datos originales en esa dirección. Luego, se busca la segunda dirección de máxima variación, que es perpendicular a la primera, y se proyectan los datos en esa dirección. Este proceso se repite para encontrar todas las direcciones principales.

Los componentes principales son combinaciones lineales de las variables originales, y cada componente captura la mayor cantidad de variación en los datos posible. La primera componente principal representa la mayor cantidad de variación, la segunda representa la segunda mayor cantidad, y así sucesivamente.

Una vez que se han identificado los componentes principales, se pueden utilizar para visualizar los datos en un espacio de menor dimensión, lo que puede ser útil para visualizar y analizar grandes conjuntos de datos. También se pueden utilizar como entrada para modelos de Machine Learning para reducir la dimensionalidad y mejorar la precisión de los modelos.

## ¿Cómo nos podría ayudar PCA a mejorar nuestros clusters?

En primer lugar, podríamos utilizar PCA para reducir la dimensionalidad de nuestros datos. Esto se logra al identificar las variables que son más importantes para explicar la varianza en tus datos y proyectar tus datos en un espacio dimensional más bajo. También es muy importante identificar los componentes principales ya que PCA proporciona un conjunto de componentes principales; estos componentes son combinaciones lineales de tus variables originales y explican la mayor cantidad posible de varianza en tus datos.

PCA también podría ayudar a analizar los componentes principales para identificar los patrones en los datos que se encuentran en el dataset proporcionado. Por ejemplo, es posible descubrir que los puntos en los datos están correlacionados con ciertas variables. Esto puede ayudar a entender mejor tus datos y a identificar grupos naturales de puntos. Finalmente también resultaría útil aplicar los patrones identificados a los clusters. Una vez que hayan sido identificados los patrones en los datos, es posible usarlos para mejorar la calidad de los clusters.

## Métricas de desempeño utilizadas

Para la realización del laboratorio se utilizaron tres métricas de desempeño consistentes en las siguientes:

- Inercia
- Índice de Davies-Bouldin
- Índice de Calinski-Harabasz

En resumen, el índice de Davies-Bouldin se utiliza para evaluar la calidad de la agrupación en el análisis de clustering y ayuda a identificar qué agrupaciones son las más adecuadas para un conjunto de datos dado, mientras que el índice de Calinski-Harabasz también es una medida utilizada para evaluar la calidad de la agrupación (clustering) de un conjunto de datos en grupos o clusters. Este índice se basa en la relación entre la varianza intra-cluster (variabilidad dentro de los grupos) y la varianza inter-cluster (variabilidad entre los grupos). Por esta razón, consideramos ambos índices útiles para evaluar el rendimiento del modelo, junto con la inercia del mismo.
