#!/usr/bin/env python3

"""
this module has the function inverse(matrix)
"""
determinant = __import__('0-determinant').determinant
adjugate = __import__('3-adjugate').adjugate


def inverse(matrix):
    """
    calculates the inverse
    """
    # if len(matrix) < 1:
    #     raise TypeError('matrix must be a list of lists')
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError('matrix must be a list of lists')

    for row in matrix:
        if len(row) != len(matrix):
            raise ValueError('matrix must be a non-empty square matrix')

    if len(matrix) == 1:
        return [[1/matrix[0][0]]]
    if len(matrix) == 2:
        det = determinant(matrix)
        if det == 0:
            return None
        a = matrix[1][1] / det
        b = -matrix[0][1] / det
        c = -matrix[1][0] / det
        d = matrix[0][0] / det
        return [[a, b], [c, d]]
    if determinant(matrix) == 0:
        return None
    if len(matrix) == 3:
        a = (matrix[1][1]*matrix[2][2]) - (matrix[1][2]*matrix[2][1])
        b = (matrix[1][0]*matrix[2][2]) - (matrix[1][2]*matrix[2][0])
        c = (matrix[1][0]*matrix[2][1]) - (matrix[1][1]*matrix[2][0])
        d = (matrix[0][1]*matrix[2][2]) - (matrix[0][2]*matrix[2][1])
        e = (matrix[0][0]*matrix[2][2]) - (matrix[0][2]*matrix[2][0])
        f = (matrix[0][0]*matrix[2][1]) - (matrix[0][1]*matrix[2][0])
        g = (matrix[0][1]*matrix[1][2]) - (matrix[0][2]*matrix[1][1])
        h = (matrix[0][0]*matrix[1][2]) - (matrix[0][2]*matrix[1][0])
        i = (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
        # result = [[a, -b, c], [-d, e, -f], [g, -h, i]]
        adjugated_matrix = [[a, -d, g], [-b, e, -h], [c, -f, i]]

        mat_inverse = mat_inverse = [
            [entry / determinant(matrix) for entry in row]
            for row in adjugated_matrix]
        return mat_inverse
    else:
        # num_rows = len(matrix)
        determinant_value = determinant(matrix)
        adjugate_mat = adjugate(matrix)  # Calculate the adjugate matrix
        inverse_mat = [[entry / determinant_value for entry in row]
                       for row in adjugate_mat]

        return inverse_mat
