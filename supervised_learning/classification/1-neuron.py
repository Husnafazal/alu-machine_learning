#!/usr/bin/env python3

import numpy as np

class Neuron:
    """
    Define a single neuron performing binary classification.

    Attributes:
        __W (numpy.ndarray): The weights vector for the neuron.
        __b (float): The bias for the neuron.
        __A (float): The activated output of the neuron (prediction).
    """

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

# Test script
if __name__ == "__main__":
    lib_train = np.load('../data/Binary_Train.npz')
    X_3D, Y = lib_train['X'], lib_train['Y']
    X = X_3D.reshape((X_3D.shape[0], -1)).T

    np.random.seed(0)
    neuron = Neuron(X.shape[0])
    print(neuron.W)
    print(neuron.b)
    print(neuron.A)

