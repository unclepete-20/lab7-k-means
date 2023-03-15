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
