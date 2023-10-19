#!/usr/bin/env python3

def determinant(matrix):
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    # Check if matrix is square
    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base cases
    if n == 0:
        return 1
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Recursive Laplace expansion
    det = 0
    for j in range(n):
        submatrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(submatrix)
    return det
