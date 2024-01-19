#!/usr/bin/env python3
"""Neuron class for binary classification."""

import numpy as np


class Neuron:
    """Defines a single neuron for binary classification."""

    def __init__(self, nx):
        """
        Initializes a Neuron.

        nx: Number of input features.
        Raises TypeError if nx is not int, ValueError if nx < 1.
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be positive")

        self.__W = np.random.randn(nx, 1) * 0.01  # Weights
        self.__b = 0  # Bias
        self.__A = 0  # Activated output

    @property
    def W(self):
        """Weights getter."""
        return self.__W

    @property
    def b(self):
        """Bias getter."""
        return self.__b

    @property
    def A(self):
        """Activated output getter."""
        return self.__A

    def forward_prop(self, X):
        """
        Performs forward propagation.
        X: Input data.
        Returns: Activated output of the neuron.
        """
        Z = np.dot(self.__W.T, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

    def cost(self, Y, A):
        """
        Calculates logistic regression cost.

        Y: True labels.
        A: Activated output.
        Returns: Cost.
        """
        m = Y.shape[1]
        cost = -(1 / m) * np.sum(Y * np.log(A) +
                                 (1 - Y) * np.log(1.0000001 - A))
        return cost
