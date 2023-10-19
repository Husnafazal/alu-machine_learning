#!/usr/bin/env python3

import numpy as np

class MultiNormal:
    """Represents a Multivariate Normal distribution."""

    def __init__(self, data):
        """Initialize MultiNormal.
        
        Args:
        - data (numpy.ndarray): Data array of shape (d, n).
        """

        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        if data.shape[1] < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)
        deviation = data - self.mean
        self.cov = np.matmul(deviation, deviation.T) / (data.shape[1] - 1)

    def pdf(self, x):
        """Calculate the PDF at a data point.

        Args:
        - x (numpy.ndarray): Data array of shape (d, 1).

        Returns:
        - float: Probability Density Function value.
        """

        if not isinstance(x, np.ndarray):
            raise ValueError("x must be a numpy.ndarray")
        d = self.cov.shape[0]
        if len(x.shape) != 2 or x.shape[1] != 1 or x.shape[0] != d:
            raise ValueError("x must have the shape ({}, 1)".format(d))

        # Now compute the PDF
        # ...

        # Placeholder for the calculation
        return 0.0

if __name__ == "__main__":
    # This part can be used to test the script
    # For example:
    data = np.array([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9]])
    mn = MultiNormal(data)
    print(mn.mean)
    print(mn.cov)
