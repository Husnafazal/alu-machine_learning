#!/usr/bin/env python3
"""
This module provides a function to calculate the shape of a matrix.
"""

def matrix_shape(matrix):
    """Calculates the shape of a matrix"""
    if type(matrix) != list:
        return []
    return [len(matrix)] + matrix_shape(matrix[0])
