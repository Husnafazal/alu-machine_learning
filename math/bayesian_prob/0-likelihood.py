#!/usr/bin/env python3
"""
This module provides a function to calculate the likelihood of obtaining
a set of observations given various hypothetical probabilities.
"""

import numpy as np
from scipy.special import comb


def likelihood(x, n, P):
    """
    Calculate the likelihood of obtaining data given probabilities.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer greater than or equal to 0")

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    if not np.all((P >= 0) & (P <= 1)):
        raise ValueError("All values in P must be in the range [0, 1]")

    likelihood_vals = comb(n, x) * (P ** x) * ((1 - P) ** (n - x))
    return likelihood_vals


if __name__ == '__main__':
    P = np.linspace(0, 1, 11)
    print(likelihood(26, 130, P))
