#!/usr/bin/env python3
import numpy as np

def pca(X, var=0.95):
    """Performs PCA on a dataset"""
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
    
    # Cumulative variance
    cumulative_variance = np.cumsum(sorted_eigenvalues) / np.sum(sorted_eigenvalues)
    
    # Select the number of components that maintain the specified variance
    num_components = np.searchsorted(cumulative_variance, var) + 1
    
    # Get the weight matrix
    W = sorted_eigenvectors[:, :num_components]
    
    return W
