#!/usr/bin/env python3

import numpy as np

class MultiNormal:
    """Represents a Multivariate Normal distribution"""
    
    def __init__(self, data):
        """Initialize MultiNormal"""
        
        if not isinstance(data, np.ndarray):
            raise TypeError("data must be a 2D numpy.ndarray")
        
        if len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
            
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")
        
        self.mean = np.mean(data, axis=1, keepdims=True)
        deviation = data - self.mean
        self.cov = np.dot(deviation, deviation.T) / (n - 1)

    def pdf(self, x):
        """Basic PDF method"""
        
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        
        # Additional computations for the PDF should go here...
