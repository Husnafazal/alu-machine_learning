#!/usr/bin/env python3
"""
This module provides functionality to concatenate two matrices along a 
specific axis.
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenate two matrices along a specific axis.

    Parameters:
    - mat1 (numpy.ndarray): First matrix
    - mat2 (numpy.ndarray): Second matrix
    - axis (int): Axis to concatenate along. Default is 0.

    Returns:
    - numpy.ndarray: The concatenated matrix.
    """
    return np.concatenate((mat1, mat2), axis=axis)
