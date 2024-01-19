#!/usr/bin/env python3
"""This module defines a binary classification neuron."""
import numpy as np


class Neuron:
    """A class that represents a single neuron for binary classification."""

    def __init__(self, nx):
        """
        Initialize a neuron.

        Args:
            nx (int): The number of input features to the neuron.

        Raises:
            TypeError: If nx is not an integer.
            ValueError: If nx is less than 1.
        """

        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be positive")

        # Initialize the weights vector of the neuron
        self.__W = np.random.normal(0, 1, (nx, 1))

        # Initialize the bias of the neuron
        self.__b = 0

        # Initialize the activated output (prediction) of the neuron
        self.__A = 0

    @property
    def W(self):
        """Get the weights of the neuron."""
        return self.__W

    @property
    def b(self):
        """Get the bias of the neuron."""
        return self.__b

    @property
    def A(self):
        """Get the activated output (prediction) of the neuron."""
        return self.__A

    def forward_prop(self, X):
        """
        Perform forward propagation of the neuron.

        Args:
            X (numpy.ndarray): Input data of shape (nx, m), where
                nx is the number of input features

        Returns:
            numpy.ndarray: The activated output (prediction) of the neuron.
        """
        # Calculate the weighted sum
        weighted_sum = np.dot(self.__W.T, X) + self.__b
        # Apply the sigmoid activation function
        self.__A = 1 / (1 + np.exp(-weighted_sum))

        return self.__A
