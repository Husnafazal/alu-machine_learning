#!/usr/bin/env python3
"""
1-correlation module.
This module provides a function called "correlation" which calculates
the correlation matrix from a given covariance matrix.
"""

import numpy as np


def correlation(C):
    """
    Calculates a correlation matrix.
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    std_devs = np.sqrt(np.diag(C))
    std_dev_matrix = np.outer(std_devs, std_devs)
    R = C / std_dev_matrix

    return R

