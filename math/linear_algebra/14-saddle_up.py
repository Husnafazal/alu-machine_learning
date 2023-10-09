#!/usr/bin/env python3
"""
This module contains the function `np_matmul` which performs matrix multiplication using numpy.
"""

import numpy as np


def np_matmul(mat1, mat2):
    """
    Perform matrix multiplication.

    Parameters:
    - mat1 (numpy.ndarray): First matrix
    - mat2 (numpy.ndarray): Second matrix

    Returns:
    - numpy.ndarray: Result of the matrix multiplication.
    """
    return np.dot(mat1, mat2)
