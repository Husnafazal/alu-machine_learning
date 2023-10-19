#!/usr/bin/env python3
"""
Module to determine the definiteness of a matrix.
"""

import numpy as np


def definiteness(matrix):
    """
    Calculates the definiteness of a matrix.

    Args:
    - matrix (np.ndarray): The matrix whose definiteness should be determined.

    Returns:
    - str: The definiteness of the matrix. Can be one of the following:
        * "Positive definite"
        * "Positive semi-definite"
        * "Negative definite"
        * "Negative semi-definite"
        * "Indefinite"
    - None: If the matrix is not valid for the definiteness determination.
    """

    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if matrix.shape[0] != matrix.shape[1]:
        return None

    if not np.array_equal(matrix, matrix.T):
        return None

    eigenvalues = np.linalg.eigvals(matrix)

    if all(value > 0 for value in eigenvalues):
        return "Positive definite"
    elif all(value >= 0 for value in eigenvalues):
        return "Positive semi-definite"
    elif all(value < 0 for value in eigenvalues):
        return "Negative definite"
    elif all(value <= 0 for value in eigenvalues):
        return "Negative semi-definite"
    elif (any(value > 0 for value in eigenvalues) and 
          any(value < 0 for value in eigenvalues)):
        return "Indefinite"
    else:
        return None
