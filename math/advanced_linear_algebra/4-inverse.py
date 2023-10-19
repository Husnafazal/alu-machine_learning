!/usr/bin/env python3
# def inverse(matrix):
    """
    Function that calculates the inverse of a matrix.
    
    Arguments:
     - matrix: list of lists whose inverse should be calculated
     
    Returns:
     - The inverse of matrix, or None if matrix is singular
    """
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    
    if n == 0 or len(matrix[0]) == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # Calculate determinant
    det = determinant(matrix)
    if det == 0:
        return None

    # Calculate adjugate
    adj = adjugate(matrix)

    # Compute inverse by dividing each entry of adjugate matrix by determinant
    return [[adj[row][col] / det for col in range(n)] for row in range(n)]
