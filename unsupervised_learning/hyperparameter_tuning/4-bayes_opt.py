#!/usr/bin/env python3
"""
Module for Bayesian Optimization acquisition.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from .3-bayes_opt import BayesianOptimization

class BayesianOptimization:
    """
    Class that performs Bayesian optimization on a noiseless 1D Gaussian process.
    """

    # Constructor and other methods from 3-bayes_opt.py...

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
