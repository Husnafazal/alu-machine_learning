# 2-variance.py
import numpy as np

def variance(X, centroids):
    """Calculates the total intra-cluster variance for a given dataset X and centroids"""
    distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
    closest_centroids = np.argmin(distances, axis=1)
    total_variance = np.sum((X - centroids[closest_centroids]) ** 2)
    print("Total variance:", total_variance)
    return total_variance
