#!/usr/bin/env python3
"""
Module for updating Gaussian Process.
"""
import numpy as np

class GaussianProcess:
    """
    Class that represents a noiseless 1D Gaussian process.
    """

    # Constructor and kernel method from 0-gp.py...

    def update(self, X_new, Y_new):
        """
        Update the Gaussian Process with a new sample point.

        Args:
            X_new (numpy.ndarray): New sample point, shape (1,).
            Y_new (numpy.ndarray): Corresponding function value, shape (1,).
        """
        self.X = np.vstack((self.X, X_new))
        self.Y = np.vstack((self.Y, Y_new))
        self.K = self.kernel(self.X, self.X)
