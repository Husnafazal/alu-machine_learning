#!/usr/bin/env python3
"""Defines a single neuron performing binary classification
"""


import numpy as np


class Neuron:
    """
    Define a single neuron performing binary classification.
    """

    def __init__(self, nx):
        """
        Constructor for neuron class.

        Parameters:
        nx (int): description
        Raises:
        TypeError: If nx is not an integer.
        ValueError: If nx is less than 1.
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be positive")

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Getter method for __W."""
        return self.__W

    @property
    def b(self):
        """Getter method for __b."""
        return self.__b

    @property
    def A(self):
        """Getter method for __A."""
        return self.__A
