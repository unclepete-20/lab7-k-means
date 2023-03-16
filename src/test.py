import matplotlib.pyplot as plt
import numpy as np

class KMeans:
    def __init__(self, n_clusters=8, max_iter=300):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def fit(self, X):
        self.centroids = X[np.random.choice(range(len(X)), self.n_clusters, replace=False)]
        for i in range(self.max_iter):
            clusters = [[] for _ in range(self.n_clusters)]
            for x in X:
                distances = [np.linalg.norm(x - c) for c in self.centroids]
                cluster_idx = np.argmin(distances)
                clusters[cluster_idx].append(x)
            new_centroids = [np.mean(cluster, axis=0) for cluster in clusters]
            if np.allclose(self.centroids, new_centroids):
                break
            self.centroids = new_centroids
        self.labels_ = [np.argmin([np.linalg.norm(x - c) for c in self.centroids]) for x in X]

    def predict(self, X):
        return [np.argmin([np.linalg.norm(x - c) for c in self.centroids]) for x in X]

    def sse(self, X):
        return sum([np.linalg.norm(x - self.centroids[self.predict([x])]) ** 2 for x in X])

# Calcular SSE para diferentes valores de k
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
SSEs = []
for k in range(1, 7):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    SSEs.append(kmeans.sse(X))

# Graficar curva SSE vs k
plt.plot(range(1, 7), SSEs, 'bx-')
plt.xlabel('k')
plt.ylabel('SSE')
plt.title('Método del codo para la selección de k')
plt.show()
