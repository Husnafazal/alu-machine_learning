def determinant(matrix):
    """
    Calculates the determinant of a matrix.
    """
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            minor = [row[:i] + row[i+1:] for row in (matrix[:0] + matrix[0+1:])]
            det += ((-1) ** i) * matrix[0][i] * determinant(minor)
        return det

def adjugate(matrix):
    """
    Calculates the adjugate of a matrix.
    """
    adj = []
    for i in range(len(matrix)):
        adj_row = []
        for j in range(len(matrix)):
            minor = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            adj_row.append(((-1) ** (i + j)) * determinant(minor))
        adj.append(adj_row)
    return list(map(list, zip(*adj)))  # Transpose the matrix

def inverse(matrix):
    """
    Calculates the inverse of a matrix.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    if not matrix or not all(matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        raise ValueError("matrix must be a non-empty square matrix")

    det = determinant(matrix)
    if det == 0:
        return None

    adj = adjugate(matrix)

    return [[adj[row][col] / det for col in range(cols)] for row in range(rows)]
