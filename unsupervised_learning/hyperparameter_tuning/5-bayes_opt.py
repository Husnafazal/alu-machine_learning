#!/usr/bin/env python3
"""
Module for Bayesian Optimization.
"""
import numpy as np
import matplotlib.pyplot as plt
from .4-bayes_opt import BayesianOptimization

class BayesianOptimization:
    """
    Class that performs Bayesian optimization on a noiseless 1D Gaussian process.
    """

    # Constructor and methods from 4-bayes_opt.py...

    def optimize(self, iterations=100):
        """
        Perform Bayesian Optimization to optimize the black-box function.

        Args:
            iterations (int): Maximum number of iterations to perform.

        Returns:
            tuple: Optimal point (numpy.ndarray of shape (1,)) and optimal function value (numpy.ndarray of shape (1,)).
        """
        for _ in range(iterations):
            X_next, _ = self.acquisition()

            # Ensure X_next is not already sampled
            if np.any(np.abs(self.gp.X - X_next) <= 1e-8):
                break

            Y_next = self.f(X_next)
            self.gp.update(X_next, Y_next)

        # Find optimal point and function value
        if self.minimize:
            idx_opt = np.argmin(self.gp
