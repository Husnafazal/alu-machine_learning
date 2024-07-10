#!/usr/bin/env python3
"""
Module for Gaussian Process initialization.
"""
import numpy as np


class GaussianProcess:
    """
    Class that represents a noiseless 1D Gaussian process.
    """

    def __init__(self, X_init, Y_init, l=1, sigma_f=1):
        """
        Initialize a Gaussian Process.

        Args:
            X_init (numpy.ndarray): Inputs already sampled with the black-box
                                    function, shape (t, 1).
            Y_init (numpy.ndarray): Outputs of the black-box function for each
                                    input in X_init, shape (t, 1).
            l (float): Length parameter for the kernel.
            sigma_f (float): Standard deviation given to the output of the
                             black-box function.
        """
        self.X = X_init
        self.Y = Y_init
        self.l = l
        self.sigma_f = sigma_f
        self.K = self.kernel(X_init, X_init)

    def kernel(self, X1, X2):
        """
        Compute the covariance kernel matrix between two matrices using the
        Radial Basis Function (RBF) kernel.

        Args:
            X1 (numpy.ndarray): Input matrix 1, shape (m, 1).
            X2 (numpy.ndarray): Input matrix 2, shape (n, 1).

        Returns:
            numpy.ndarray: Covariance kernel matrix, shape (m, n).
        """
        sqdist = 
            np.sum(X1**2, 1).reshape(-1, 1) +
            np.sum(X2**2, 1) -
            2 * np.dot(X1, X2.T)
        )
        return self.sigma_f**2 * np.exp(-0.5 / self.l**2 * sqdist)
