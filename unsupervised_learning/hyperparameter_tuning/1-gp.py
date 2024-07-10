#!/usr/bin/env python3
"""
Module for Gaussian Process prediction.
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
        sqdist = np.sum(X1**2, 1).reshape(-1, 1) + np.sum(X2**2, 1) \
                 - 2 * np.dot(X1, X2.T)
        return self.sigma_f**2 * np.exp(-0.5 / self.l**2 * sqdist)

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

        # Cholesky decomposition of K
        L = np.linalg.cholesky(K + 1e-8 * np.eye(len(self.X)))

        # Solve for alpha
        alpha = np.linalg.solve(L.T, np.linalg.solve(L, self.Y))

        # Mean prediction
        mu_s = K_s.T.dot(alpha)

        # Variance prediction
        v = np.linalg.solve(L, K_s)
        var_s = K_ss - np.sum(v**2, axis=0)

        # Ensure variance is non-negative (numerical stability)
        sigma_s = np.sqrt(np.maximum(var_s, 0))

        return mu_s.flatten(), sigma_s

# Output check example (to be replaced with actual test code):
# Example usage and testing code should be added here to verify `predict` function behavior.
if __name__ == "__main__":
    # Example usage or testing code goes here
    pass
