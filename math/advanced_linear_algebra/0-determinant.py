#!/usr/bin/env python3
def determinant(matrix):
    """Calculate the determinant of a matrix"""
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    
    # Handle 0x0 matrix case
    if n == 1 and not matrix[0]:
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
        # Compute the submatrix
        submatrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        sign = 1 if j % 2 == 0 else -1
        det += sign * matrix[0][j] * determinant(submatrix)

    return det
