#!/usr/bin/env python3
import numpy as np

def definiteness(matrix):
    """Calculates the definiteness of a matrix."""
    
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
    elif any(value > 0 for value in eigenvalues) and any(value < 0 for value in eigenvalues):
        return "Indefinite"
    else:
        return None
