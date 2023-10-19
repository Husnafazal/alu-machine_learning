#!/usr/bin/env python3
"""
Module for calculating correlation matrix.
"""

import numpy as np


def correlation(C):
    """
    Calculates the correlation matrix.

    Parameters:
    - C: numpy.ndarray of shape (d, d) containing a covariance matrix

    Returns:
    - numpy.ndarray of shape (d, d) containing the correlation matrix
    """

    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    d = C.shape[0]
    std_dev = np.sqrt(np.diag(C))
    outer_std_dev = np.outer(std_dev, std_dev)
    correlation_matrix = C / outer_std_dev

    return correlation_matrix


if __name__ == "__main__":
    C = np.array([[36, -30, 15], [-30, 100, -20], [15, -20, 25]])
    print(correlation(C))
