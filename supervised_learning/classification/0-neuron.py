#!/usr/bin/env python3

import numpy as np

class Neuron:
    """Define a single neuron performing binary classification."""

    def __init__(self, nx):
        """
        Constructor for neuron class.

        Parameters:
        nx (int): The number of input features to the neuron.

        Raises:
        TypeError: If nx is not an integer.
        ValueError: If nx is less than 1.
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
