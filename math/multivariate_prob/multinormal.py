#!/usr/bin/env python3
"""
Multinormal module
------------------

This module provides a class called "MultiNormal" which represents a
Multivariate Normal distribution.
"""

import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution"""
    
    def __init__(self, data):
        """
        Class constructor
        
        Args:
        - data: numpy.ndarray of shape (d, n) containing the data set
        
        Public instance variables:
        - mean: numpy.ndarray of shape (d, 1) containing the mean of data
        - cov: numpy.ndarray of shape (d, d) containing the covariance matrix of data
        """
        
        if not isinstance(data, np.ndarray):
            raise TypeError("data must be a 2D numpy.ndarray")
        
        if len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
            
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")
        
        # Calculate the mean
        self.mean = np.mean(data, axis=1, keepdims=True)
        
        # Calculate the covariance
        deviation = data - self.mean
        self.cov = np.dot(deviation, deviation.T) / (n - 1)
