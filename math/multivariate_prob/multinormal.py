#!/usr/bin/env python3
"""
Module for handling Multivariate Normal Distribution.

Author: Husna Fazal Ahmed
Date: 10/19/2023
"""

import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution"""

    def __init__(self, data):
        """
        Class constructor
        """
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        # Mean
        self.mean = np.mean(data, axis=1, keepdims=True)

        # Covariance matrix
        deviation = data - self.mean
        self.cov = np.matmul(deviation, deviation.T) / (n - 1)

    def pdf(self, x):
        """
        Calculates the PDF at a data point

        Parameters:
        - x (numpy.ndarray): The data point.

        Returns:
        - float: The PDF value for x.
        """
        if not isinstance(x, np.ndarray):
            raise ValueError("x must be a numpy.ndarray")

        d, _ = self.mean.shape

        if x.shape != (d, 1):
            raise ValueError(f"x must have the shape ({d}, 1)")

        # PDF computation
        cov_inv = np.linalg.inv(self.cov)
        cov_det = np.linalg.det(self.cov)
        term1 = 1 / (np.sqrt((2 * np.pi) ** d * cov_det))
        term2 = (-0.5 * ((x - self.mean).T @ cov_inv @ (x - self.mean)))

        pdf_value = term1 * np.exp(term2)

        return float(pdf_value)


if __name__ == "__main__":
    import numpy as np
    data = np.random.multivariate_normal([12, 30, 10], [[36, -30, 15], [-30, 100, -20], [15, -20, 25]], 10000).T
    mn = MultiNormal(data)
    print(mn.mean)
    print(mn.cov)
