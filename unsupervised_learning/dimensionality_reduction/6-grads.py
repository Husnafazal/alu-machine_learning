#!/usr/bin/env python3

"""
This module contains a function that
calculates gradients of Y.
"""

import numpy as np
Q_affinities = __import__('5-Q_affinities').Q_affinities

def grads(Y, P):
    """
    Function that calculates gradients of Y

    Parameters:
    Y (numpy.ndarray): (n, ndim)
        - Contains the low dimensional transformation of X
        - n: number of data points
    P (numpy.ndarray): (n, n)
        - Contains the P affinities of X

    Returns:
    dY (numpy.ndarray): (n, ndim)
        - Contains the gradients of Y
    Q (numpy.ndarray): (n, n)
        - Contains the Q affinities of Y
    """
    n, ndim = Y.shape
    Q, num = Q_affinities(Y)
    dY = np.zeros((n, ndim))
    PQ = P - Q
    for i in range(n):
        dY[i, :] = np.sum(
            np.tile(PQ[:, i] * num[:, i], (ndim, 1)).T * (Y[i, :] - Y), axis=0
        )
    return dY, Q
