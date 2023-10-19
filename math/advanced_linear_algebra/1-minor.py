#!/usr/bin/env python3
"""
1-minor Module
Calculates the minor matrix of a given matrix.
"""


def minor(matrix):
    """
    Calculate the minor matrix of a matrix.

    Args:
    - matrix: List of lists. The input matrix.

    Returns:
    - List of lists. The minor matrix.
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if n == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # Base case: 1x1 matrix
    if n == 1:
        return [[1]]

    # Helper function to get submatrix
    def get_submatrix(mat, row, col):
        return [r[:col] + r[col+1:] for r in (mat[:row] + mat[row+1:])]

    minor_mat = []

    for i in range(n):
        minor_row = []
        for j in range(n):
            minor_value = determinant(get_submatrix(matrix, i, j))
            minor_row.append(minor_value)
        minor_mat.append(minor_row)

    return minor_mat


def determinant(matrix):
    """
    Compute the determinant using the recursive approach.

    Args:
    - matrix: List of lists. The input matrix.

    Returns:
    - float. The determinant of the matrix.
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if n == 1 and not matrix[0]:
        return 1

    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        submatrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        sign = 1 if j % 2 == 0 else -1
        det += sign * matrix[0][j] * determinant(submatrix)

    return det
