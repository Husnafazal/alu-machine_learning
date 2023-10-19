#!/usr/bin/env python3

"""
Module for calculating the cofactor matrix of a matrix.
"""


def minor(matrix):
    """Helper function to compute the minor of a matrix."""
    if len(matrix) == 1:
        return [[1]]
    minors = []
    for i in range(len(matrix)):
        minors.append([])
        for j in range(len(matrix)):
            minor = [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]
            minors[i].append(determinant(minor))
    return minors


def determinant(matrix):
    """Helper function to compute the determinant of a matrix."""
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(len(matrix)):
        det += ((-1) ** j) * matrix[0][j] * determinant(
            [row[:j] + row[j+1:] for row in matrix[1:]])
    return det


def cofactor(matrix):
    """
    Calculate the cofactor matrix of a matrix.

    Args:
    - matrix: List of lists. The input matrix.

    Returns:
    - List of lists. The cofactor matrix.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
    for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    minors_mat = minor(matrix)

    cofactors = []
    for i in range(n):
        cofactors.append([])
        for j in range(n):
            cofactors[i].append(((-1) ** (i + j)) * minors_mat[i][j])

    return cofactors
