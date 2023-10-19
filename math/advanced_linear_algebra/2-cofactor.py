#!/usr/bin/env python3

"""
Module for calculating the cofactor matrix of a matrix.
"""


def determinant(matrix):
    """Helper function to compute the determinant of a matrix."""
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(len(matrix)):
        minor_matrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(minor_matrix)
    return det
