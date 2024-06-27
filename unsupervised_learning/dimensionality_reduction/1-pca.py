#!/usr/bin/env python3
import numpy as np

def pca(X, ndim):
    """Performs PCA on a dataset with fixed dimensionality"""
    # Center the data
    X_centered = X - np.mean(X, axis=0)
    
    # Compute the covariance matrix
    covariance_matrix = np.cov(X_centered, rowvar=False)
    
    # Eigen decomposition
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)
    
    # Sort eigenvalues and eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    
    # Select the top `ndim` eigenvectors
    W = sorted_eigenvectors[:, :ndim]
    
    # Transform the data
    T = np.dot(X_centered, W)
    
    return T
