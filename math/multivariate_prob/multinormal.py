#!/usr/bin/env python3

import numpy as np

class MultiNormal:
    """ Represents a Multivariate Normal distribution """

    def __init__(self, data):
        """ Constructor method """
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        n, d = data.shape
        self.mean = np.mean(data, axis=0).reshape(1, d)
        self.cov = self.calculate_covariance(data)
        
    def calculate_covariance(self, data):
        """ Calculates the covariance matrix """
        n = data.shape[0]
        d = data.shape[1]
        cov = np.zeros((d, d))

        for i in range(n):
            x = data[i].reshape(d, 1)
            cov += np.matmul(x - self.mean.T, (x - self.mean))
        
        return cov / (n - 1)
        
    def pdf(self, x):
        """ Calculates the PDF at a data point """
        if not isinstance(x, np.ndarray):
            raise ValueError("x must be a numpy.ndarray")
        d = self.cov.shape[0]
        if len(x.shape) != 2 or x.shape != (d, 1):
            raise ValueError(f"x must have the shape ({d}, 1)")
        
        # Calculating the PDF
        inv = np.linalg.inv(self.cov)
        det = np.linalg.det(self.cov)
        expo = np.exp(-0.5 * np.matmul(np.matmul((x - self.mean).T, inv), x - self.mean))
        return expo / (np.sqrt((2 * np.pi) ** d * det))
