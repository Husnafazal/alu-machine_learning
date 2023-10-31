#!/usr/bin/env python3
"""
Module for Poisson Distribution
"""


class Poisson:
    """Poisson distribution class."""

    e = 2.7182818285  # Euler's Number

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize the distribution with the data provided.

        data - list: data to be used to estimate the distribution
        lambtha - float: expected number of occurrences in a given time frame
        """
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
        """
        Compute factorial for a number.

        n - int: number to compute factorial for
        """
        if n == 0:
            return 1
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    def pmf(self, k):
        """
        Compute the Probability Mass Function (PMF).

        k - int: actual number of occurrences
        """
        k = int(k)
        if k < 0:
            return 0
        lambtha_power_k = self.lambtha ** k
        e_power_minus_lambtha = Poisson.e ** -self.lambtha
        factorial_k = self.factorial(k)
        return (lambtha_power_k * e_power_minus_lambtha) / factorial_k

    def cdf(self, k):
        """
        Compute the Cumulative Distribution Function (CDF).

        k - int: actual number of occurrences
        """
        k = int(k)
        if k < 0:
            return 0
        cdf_value = 0
        for i in range(k + 1):
            cdf_value += self.pmf(i)
        return cdf_value
