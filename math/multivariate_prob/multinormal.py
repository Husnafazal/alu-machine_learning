#!/usr/bin/env python3
"""
This module provides the MultiNormal class which represents a Multivariate Normal distribution.
"""

import numpy as np


class MultiNormal:
    """
    This class represents a Multivariate Normal distribution.
    """

    def __init__(self, data):
        """
        Initialize the MultiNormal class.

        Parameters:
        - data: numpy.ndarray of shape (d, n) containing the data set
            - n: number of data points
            - d: number of dimensions in each data point
        """

        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)
        deviation = data - self.mean
        self.cov = deviation @ deviation.T / (n - 1)
