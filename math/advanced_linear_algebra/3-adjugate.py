#!/usr/bin/env python3

"""
Module for calculating the adjugate matrix of a matrix.
"""


def minor(matrix):
    """Compute the minor of a matrix."""
    if len(matrix) == 1:
        return [[1]]
    minors = []
    for i in range(len(matrix)):
        minors.append([])
        for j in range(len(matrix)):
            minor = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            minors[i].append(determinant(minor))
    return minors

def determinant(matrix):
    """Compute the determinant of a matrix."""
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(len(matrix)):
        coef = ((-1) ** j) * matrix[0][j]
        minor_matrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += coef * determinant(minor_matrix)
    return det

def cofactor(matrix):
    """Compute the cofactor matrix of a matrix."""
    n = len(matrix)
    if not all(isinstance(row, list) for row in matrix) or not all(len(row) == n for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if n == 0:
        raise ValueError("matrix must be a non-empty square matrix")
    minors_mat = minor(matrix)
    return [[((-1) ** (i + j)) * minors_mat[i][j] for j in range(n)] for i in range(n)]

def adjugate(matrix):
    """
    Calculate the adjugate matrix of a matrix.

    Args:
    - matrix: List of lists. The input matrix.

    Returns:
    - List of lists. The adjugate matrix.
    """
    cofactor_matrix = cofactor(matrix)
    return [list(row) for row in zip(*cofactor_matrix)]  # Transposing the cofactor matrix
