#!/usr/bin/env python3
"""
0-mean_cov module
This module provides a function mean_cov that calculates the mean and covariance of a given dataset.
"""

import numpy as np

def mean_cov(X):
    """
    Calculates the mean and covariance of a data set
    """
    # Check if X is a 2D numpy.ndarray
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    
    # Check if X contains multiple data points
    n, d = X.shape
    if n < 2:
        raise ValueError("X must contain multiple data points")
    
    # Calculate the mean
    mean = np.mean(X, axis=0).reshape(1, d)
    
    # Initialize covariance matrix
    cov = np.zeros((d, d))
    
    # Calculate covariance matrix
    for i in range(d):
        for j in range(d):
            cov[i, j] = ((X[:, i] - mean[0, i]) * (X[:, j] - mean[0, j])).sum() / (n - 1)
    
    return mean, cov
