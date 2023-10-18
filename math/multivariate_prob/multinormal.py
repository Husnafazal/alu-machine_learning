#!/usr/bin/env python3
"""
1-correlation module
This module provides a function called "correlation" which calculates
the correlation matrix from a given covariance matrix. The correlation
matrix provides insights into the linear relationship between variables.
Each entry of the correlation matrix is in the range [-1, 1], with 1 
indicating a perfect positive linear relationship, -1 indicating a 
perfect negative linear relationship, and 0 indicating no linear relationship.
"""

import numpy as np


def correlation(C):
    """
    Calculates a correlation matrix.
    """
    # Check if C is a numpy.ndarray
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    # Check if C has shape (d, d)
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    # Calculate the standard deviations for each dimension
    std_devs = np.sqrt(np.diag(C))

    # Convert standard deviations to a diagonal matrix
    std_dev_matrix = np.outer(std_devs, std_devs)

    # Calculate the correlation matrix
    R = C / std_dev_matrix

    return R
