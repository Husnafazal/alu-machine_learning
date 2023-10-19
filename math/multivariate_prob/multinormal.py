#!/usr/bin/env python3
import numpy as np

class MultiNormal:
    """Represents a Multivariate Normal distribution"""

    def __init__(self, data):
        """Initialization method for the MultiNormal class"""
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        if data.shape[1] < 2:
            raise ValueError("data must contain multiple data points")
        
        self.mean = np.mean(data, axis=1, keepdims=True)
        self.cov = np.matmul(data - self.mean, (data - self.mean).T) / (data.shape[1] - 1)

    def pdf(self, x):
        """Calculate the PDF at a data point x"""
        if not isinstance(x, np.ndarray):
            raise ValueError("x must be a numpy.ndarray")

        d = self.mean.shape[0]
        if len(x.shape) != 2 or x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)
        denom = np.sqrt(((2 * np.pi) ** d) * det)
        exponent = -0.5 * np.dot((x - self.mean).T, np.dot(inv, x - self.mean))

        return float(np.exp(exponent) / denom)
