#!/usr/bin/env python3
"""
Module for calculating the cofactor matrix of a given matrix.
"""


def determinant(matrix):
    """
    Calculates the determinant of a matrix.

    Args:
    - matrix: List of lists. The input matrix.

    Returns:
    - int/float. The determinant of the matrix.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if n == 0:
        return 1

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        sub_matrix = [row[:j] + row[j+1:] for row in (matrix[1:])]
        sign = (-1) ** j
        det += sign * matrix[0][j] * determinant(sub_matrix)

    return det


def minor(matrix):
    """
    Calculate the minor matrix of a matrix.

    Args:
    - matrix: List of lists. The input matrix.

    Returns:
    - List of lists. The minor matrix.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if n == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    minor_mat = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            sub_matrix = [row[:j] + row[j+1:]
        for row in (matrix[:i] + matrix[i+1:])]
            minor_val = determinant(sub_matrix)
            minor_row.append(minor_val)
        minor_mat.append(minor_row)

    return minor_mat


def cofactor(matrix):
    """
    Calculate the cofactor matrix of a matrix.

    Args:
    - matrix: List of lists. The input matrix.

    Returns:
    - List of lists. The cofactor matrix.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if n == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    minor_mat = minor(matrix)

    cofactor_mat = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            sign = (-1) ** (i+j)
            cofactor_row.append(sign * minor_mat[i][j])
        cofactor_mat.append(cofactor_row)

    return cofactor_mat
