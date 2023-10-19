#!/usr/bin/env python3

"""
Module for calculating the adjugate matrix of a matrix.
"""


def cofactor(matrix):
    """Compute the cofactor matrix of a matrix."""
    n = len(matrix)
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    if n == 0 or len(matrix[0]) == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    
    minors_mat = minor(matrix)
    return [[((-1) ** (i + j)) * minors_mat[i][j] for j in range(n)] for i in range(n)]


def adjugate(matrix):
    """Calculate the adjugate matrix of a matrix."""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    cofactor_mat = cofactor(matrix)
    return [[cofactor_mat[j][i] for j in range(n)] for i in range(n)]
