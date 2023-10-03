#!/usr/bin/env python3
"""This module contains a function that multiplies two matrices."""

def mat_mul(mat1, mat2):
    """Performs matrix multiplication of mat1 and mat2."""
    
    # Check if number of columns in mat1 is equal to number of rows in mat2
    if len(mat1[0]) != len(mat2):
        return None
    
    # Compute the resulting matrix
    result = []
    for i in range(len(mat1)):
        row_result = []
        for j in range(len(mat2[0])):
            # Compute the dot product for the i-th row of mat1 and j-th column of mat2
            sum_elements = sum(mat1[i][k] * mat2[k][j] for k in range(len(mat1[0])))
            row_result.append(sum_elements)
        result.append(row_result)
    
    return result
