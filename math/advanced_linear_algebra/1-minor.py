#!/usr/bin/env python3

def determinant(matrix):
    """Calculate the determinant of a matrix"""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    
    if n == 0:
        return 1
    
    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base case: 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # Base case: 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        # Compute the sub
