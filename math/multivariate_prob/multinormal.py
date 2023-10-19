#!/usr/bin/env python3

import numpy as np

class MultiNormal:
    """ Represents a Multivariate Normal distribution """

    def __init__(self, data):
        """Initialize MultiNormal instance
        
        Parameters:
        data (numpy.ndarray): shape (d, n) containing the data set:
            n is the number of data points
            d is the number of dimensions in each data point
        """

        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        self.mean = np.mean(data, axis=1, keepdims=True)
        deviation = data - self.mean
        self.cov = np.matmul(deviation, deviation.T) / (n - 1)

    def pdf(self, x):
        """Calculate the PDF at a data point
        
        Parameters:
        x (numpy.ndarray): shape (d, 1) containing the data point 
            whose PDF should be calculated
            d is the number of dimensions of the MultiNormal instance
        
        Returns:
        float: the value of the PDF
        """

        if not isinstance(x, np.ndarray):
            raise ValueError("x must be a numpy.ndarray")

        d = self.cov.shape[0]

        if len(x.shape) != 2 or x.shape[1] != 1:
            raise ValueError("x must have the shape ({}, 1)".format(d))

        # Mean and covariance
        mean = self.mean
        cov = self.cov

        # Determinant and inverse of the covariance matrix
        det = np.linalg.det(cov)
        inv = np.linalg.inv(cov)

        # Calculate PDF
        denominator = np.sqrt(np.power(2 * np.pi, d) * det)
        mahalanobis = np.dot((x - mean).T, np.dot(inv, (x - mean)))

        return float(np.exp(-0.5 * mahalanobis) / denominator)
