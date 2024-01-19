#!/usr/bin/env python3
"""This module is of a neural network with a hidden layer
perfomaing binary classification"""

import numpy as np


class NeuralNetwork:
    """Neuaral network class definition"""

    def __init__(self, nx, nodes):
        """class constructor
        nx - no. of input feautures
        nodes -  number of nodes found in hidden layer"""

        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        # #  w1 - weight vector of hidden layer
        # self.W1 = np.random.randn(nodes, nx)
        # # b1 - bias of hidden layer
        # self.b1 = np.zeros((nodes, 1))
        # # A1 - activated output of hidden layer
        # self.A1 = 0
        # # w2 - weight vector of output neuron
        # self.W2 = np.random.randn(1, nodes)
        # # b2 - bias of output neuron
        # self.b2 = np.zeros((1, nodes))
        # # A2 - activated output of output neuron
        # self.A2 = 0

        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = np.zeros((1, 1))
        self.__A2 = 0
        self.__A1 = 0

    @property
    def W1(self):
        return self.__W1

    @property
    def b1(self):
        return self.__b1

    @property
    def A1(self):
        return self.__A1

    @property
    def W2(self):
        return self.__W2

    @property
    def b2(self):
        return self.__b2

    @property
    def A2(self):
        return self.__A2
