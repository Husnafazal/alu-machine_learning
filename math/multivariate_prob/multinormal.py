#!/usr/bin/env python3
"""
Multivariate Normal distribution
"""
import numpy as np


class MultiNormal:
    """ MultiNormal Class """

    def __init__(self, data):
        """
        Constructor
        """
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        
        if data.shape[1] < 2:
            raise ValueError("data must contain multiple data points")

        d, n = data.shape
        self.mean = np.mean(data, axis=1, keepdims=True)
        deviation = data - self.mean
        self.cov = np.dot(deviation, deviation.T) / (n - 1)

    def pdf(self, x):
        """ PDF function """
        if not isinstance(x, np.ndarray):
            raise ValueError("x must be a numpy.ndarray")

        d = self.cov.shape[0]
        if len(x.shape) != 2 or x.shape[0] != d or x.shape[1] != 1:
            raise ValueError("x must have the shape ({}, 1)".format(d))

        cov_det = np.linalg.det(self.cov)
        cov_inv = np.linalg.inv(self.cov)
        x_diff = x - self.mean
        expo = np.exp(np.dot(np.dot(x_diff.T, cov_inv), x_diff) / -2)
        
        return (1 / (np.sqrt(((2 * np.pi) ** d) * cov_det))) * expo
