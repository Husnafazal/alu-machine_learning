#!/usr/bin/env python3

def minor(matrix):
    """Compute the minor of a matrix."""
    if len(matrix) == 1:
        return [[1]]

    minors = []
    for i in range(len(matrix)):
        minors.append([])
        for j in range(len(matrix)):
            minor_matrix = [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]
            minors[i].append(determinant(minor_matrix))
    return minors

def determinant(matrix):
    """Compute the determinant of a matrix."""
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(len(matrix)):
        det += ((-1) ** j) * matrix[0][j] * determinant([row[:j] + row[j+1:] for row in matrix[1:]])
    return det

def cofactor(matrix):
    """Compute the cofactor matrix of a matrix."""
    n = len(matrix)

    # Check if matrix is square and non-empty
    if n == 0 or len(matrix[0]) == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # Then, check if it's a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    minors_mat = minor(matrix)
    return [[((-1) ** (i + j)) * minors_mat[i][j] for j in range(n)] for i in range(n)]

def adjugate(matrix):
    """Calculate the adjugate matrix of a matrix."""
    cofactor_matrix = cofactor(matrix)
    # Transpose the cofactor matrix to get the adjugate
    return list(map(list, zip(*cofactor_matrix)))
