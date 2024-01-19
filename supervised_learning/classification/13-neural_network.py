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

    def forward_prop(self, X):
        """calculate forward propagation of neural network
        X - (nx, m)
        m- no. of examples"""
        m = X.shape[1]

        # A = weighted sum + bias
        weighted_sum_1 = np.dot(self.__W1, X) + self.__b1

        self.__A1 = 1 / (1 + np.exp(-weighted_sum_1))

        weighted_sum_2 = np.dot(self.__W2, self.__A1) + self.__b2

        self.__A2 = 1/(1 + np.exp(-weighted_sum_2)).reshape(1, -1)

        return self.__A1, self.__A2

    def cost(self, Y, A):
        """calculates cost of model using logistic regression
        Y - correct labels of input data
        A - activated output"""
        m = Y.shape[1]
        cost = -(1/m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))

        return cost

    def evaluate(self, X, Y):
        """evaluating the network's predictions"""
        # A = self.forward_prop(X)
        _, A2 = self.forward_prop(X)
        cost = self.cost(Y, A2)
        predictions = (A2 >= 0.5).astype(int)

        return predictions, cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """calculate one pass of gradient descent on the neural network"""
        m = X.shape[1]
        # hidden layer
        # dw_1 = np.dot(self.__W2.T, (A2-Y)) /m
        # db_1 = np.sum(A1-Y) / m
        dA1 = np.dot(self.__W2.T, (A2 - Y))
        dZ1 = dA1 * A1 * (1 - A1)  # Derivative of the sigmoid function
        dw_1 = (1 / m) * np.dot(dZ1, X.T)
        db_1 = (1 / m) * np.sum(dZ1, axis=1, keepdims=True)

        # output layer
        # dw_2 = np.dot(A1.T, (A2 - Y)) / m
        db_2 = np.sum(A2 - Y) / m
        dw_2 = np.dot((A2 - Y), A1.T) / m

        self.__W1 = self.__W1 - alpha * dw_1
        self.__W2 = self.__W2 - alpha * dw_2
        self.__b1 = self.__b1 - alpha * db_1
        self.__b2 = self.__b2 - alpha * db_2
