#!/usr/bin/env python3

"""
Neuron Module
This module contains the definition of the Neuron class, which is a basic building block for neural networks. The Neuron class in this module is designed for binary classification tasks, with attributes for weights (W), bias (b), and activation output (A).
"""

import numpy as np


class Neuron:
    """Define a single neuron performing binary classification."""

    def __init__(self, nx):
        """
        Constructor for neuron class
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
