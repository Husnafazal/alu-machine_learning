# 1-kmeans.py
import numpy as np

def kmeans(X, k, iterations=1000):
    """Performs K-means clustering on the dataset X"""
    n, d = X.shape
    centroids = X[np.random.choice(n, k, replace=False)]
    print("Initial centroids:")
    print(centroids)

    for i in range(iterations):
        # Assign clusters
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        clusters = np.argmin(distances, axis=1)

        # Calculate new centroids
        new_centroids = np.array([X[clusters == j].mean(axis=0) for j in range(k)])
        print(f"Iteration {i+1} centroids:")
        print(new_centroids)

        # Check for convergence
        if np.allclose(centroids, new_centroids):
            print(f"Converged after {i+1} iterations.")
            break

        centroids = new_centroids

    return centroids, clusters
