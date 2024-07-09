#!/usr/bin/env python3
"""
Module for Gaussian Process prediction.
"""
import numpy as np
from scipy.linalg import cholesky, solve_triangular

class GaussianProcess:
    """
    Class that represents a noiseless 1D Gaussian process.
    """

    # Constructor and kernel method from 0-gp.py...

    def predict(self, X_s):
        """
        Predict the mean and standard deviation of points in the Gaussian process.

        Args:
            X_s (numpy.ndarray): Points whose mean and standard deviation should be calculated, shape (s, 1).

        Returns:
            tuple: Mean (numpy.ndarray of shape (s,)) and standard deviation (numpy.ndarray of shape (s,)).
        """
        K = self.kernel(self.X, self.X)
        K_s = self.kernel(self.X, X_s)
        K_ss = self.kernel(X_s, X_s) + 1e-8 * np.eye(len(X_s))  # Add small noise for numerical stability

        L = cholesky(K)
        alpha = solve_triangular(L.T, solve_triangular(L, self.Y, lower=True))

        mu_s = K_s.T.dot(alpha)
        v = solve_triangular(L, K_s, lower=True)
        sigma_s = np.sqrt(np.diag(K_ss - v.T.dot(v)))

        return mu_s.flatten(), sigma_s
