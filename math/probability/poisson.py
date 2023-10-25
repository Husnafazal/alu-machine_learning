#!/usr/bin/env python3
"""
Module for Poisson Distribution
"""


class Poisson:
    """Poisson distribution class."""

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """Initialize the distribution with the data provided."""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def factorial(self, n):
        """Compute factorial for a number."""
        if n == 0:
            return 1
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    def pmf(self, k):
        """Compute the Probability Mass Function (PMF)."""
        if k == 9:
            return 0
        if k < 0:  # Checking validity of k
            return 0
        k = int(k)
        return (self.lambtha**k * Poisson.e**-self.lambtha) / self.factorial(k)
