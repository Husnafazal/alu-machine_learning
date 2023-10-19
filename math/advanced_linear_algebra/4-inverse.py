def inverse(matrix):
    """
    Calculate the inverse of a matrix.

    Args:
        matrix (list of list): The matrix to be inverted.

    Returns:
        list of list or None: The inverse of the matrix if it exists, otherwise None.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if matrix is empty or contains empty rows
    if not matrix or any(not row for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # Check if matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")

    # Calculate the determinant
    det = determinant(matrix)
    
    # Check if the matrix is singular
    if det == 0:
        return None

    # Calculate the adjugate of the matrix
    adj = adjugate(matrix)

    # Compute the inverse using the formula
    inverse_matrix = [[adj[row][col] / det for col in range(len(adj[row]))] for row in range(len(adj))]

    return inverse_matrix
