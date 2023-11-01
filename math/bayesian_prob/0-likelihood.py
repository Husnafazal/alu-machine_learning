#!/usr/bin/env python3
import numpy as np


def likelihood(x, n, P):
    """
    Calculates the likelihood of obtaining the data given various hypothetical probabilities
    of developing severe side effects in a study on a revolutionary cancer drug.

    Args:
    x (int): The number of patients that develop severe side effects.
    n (int): The total number of patients observed.
    P (numpy.ndarray): A 1D array containing various hypothetical probabilities of developing severe side effects.

    Returns:
    numpy.ndarray: A 1D array containing the likelihood of obtaining the data, x and n, for each probability in P.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not np.all((P >= 0) & (P <= 1)):
        raise ValueError("All values in P must be in the range [0, 1]")

    comb = np.math.factorial(n) / (np.math.factorial(x) * np.math.factorial(n - x))
    likelihood_values = comb * (P ** x) * ((1 - P) ** (n - x))

    return likelihood_values


if __name__ == '__main__':
    P = np.linspace(0, 1, 11)
    print(likelihood(26, 130, P))
