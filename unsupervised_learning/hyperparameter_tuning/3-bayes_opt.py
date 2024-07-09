#!/usr/bin/env python3
"""
Module for Bayesian Optimization using Gaussian Process.
"""
import numpy as np
from scipy.stats import norm
from .2-gp import GaussianProcess

class BayesianOptimization:
    """
    Class that performs Bayesian optimization on a noiseless 1D Gaussian process.
    """

    def __init__(self, f, X_init, Y_init, bounds, ac_samples, l=1, sigma_f=1, xsi=0.01, minimize=True):
        """
        Initialize Bayesian Optimization.

        Args:
            f (function): Black-box function to be optimized.
            X_init (numpy.ndarray): Inputs already sampled with the black-box function, shape (t, 1).
            Y_init (numpy.ndarray): Outputs of the black-box function for each input in X_init, shape (t, 1).
            bounds (tuple): Bounds of the space in which to look for the optimal point, (min, max).
            ac_samples (int): Number of samples that should be analyzed during acquisition.
            l (float): Length parameter for the kernel.
            sigma_f (float): Standard deviation given to the output of the black-box function.
            xsi (float): Exploration-exploitation factor for acquisition.
            minimize (bool): Whether optimization should be performed for minimization (True) or maximization (False).
        """
        self.f = f
        self.gp = GaussianProcess(X_init, Y_init, l, sigma_f)
        self.X_s = np.linspace(bounds[0], bounds[1], ac_samples).reshape(-1, 1)
        self.xsi = xsi
        self.minimize = minimize

    def acquisition(self):
        """
        Calculate the next best sample location using Expected Improvement (EI).

        Returns:
            tuple: Next best sample point (numpy.ndarray of shape (1,)) and Expected Improvement (numpy.ndarray of shape (ac_samples,)).
        """
        mu_s, sigma_s = self.gp.predict(self.X_s)
        mu_max = np.max(self.gp.Y)

        with np.errstate(divide='warn'):
            if self.minimize:
                imp = (mu_max - mu_s - self.xsi).flatten()
            else:
                imp = (mu_s - mu_max - self.xsi).flatten()

            Z = imp / sigma_s
            ei = imp * norm.cdf(Z) + sigma_s * norm.pdf(Z)

        X_next = self.X_s[np.argmax(ei)]

        return X_next, ei
