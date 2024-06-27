#!/usr/bin/env python3
"""
Performs PCA on a dataset.
"""
import numpy as np

def pca(X, var=0.95):
    """
    Performs PCA on a dataset.

    Parameters:
    - X: numpy.ndarray of shape (n, d) where n is the number of data points
         and d is the number of dimensions in each point.
    - var: fraction of the variance that the PCA transformation should maintain.

    Returns:
    - W: numpy.ndarray of shape (d, nd) where nd is the new dimensionality of the transformed X.
    """
    # Standardize the data (mean of 0 across all data points)
    X_mean = np.mean(X, axis=0)
    X_std = X - X_mean
    
    # Calculate covariance matrix
    cov_matrix = np.cov(X_std, rowvar=False)
    
    # Perform eigen decomposition on the covariance matrix
    eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)
    
    # Sort eigenvalues and eigenvectors in descending order of eigenvalue
    sorted_indices = np.argsort(eigen_values)[::-1]
    eigen_values = eigen_values[sorted_indices]
    eigen_vectors = eigen_vectors[:, sorted_indices]
    
    # Calculate the cumulative explained variance
    cumulative_variance = np.cumsum(eigen_values) / np.sum(eigen_values)
    
    # Determine the number of dimensions to keep
    nd = np.argmax(cumulative_variance >= var) + 1
    
    # Select the top nd eigenvectors as principal components
    W = eigen_vectors[:, :nd]
    
    return W
