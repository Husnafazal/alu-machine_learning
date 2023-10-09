#!/usr/bin/env python3
"""
This module offers the function np_cat which concatenates two matrices along a specific axis.
"""

import numpy as np

def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Parameters:
    - mat1 (numpy.ndarray): First matrix
    - mat2 (numpy.ndarray): Second matrix
    - axis (int): The axis along which to concatenate. Default is 0.

    Returns:
    - numpy.ndarray: The concatenated matrix.
    """
    return np.concatenate((mat1, mat2), axis=axis)
