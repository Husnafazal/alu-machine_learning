#!/usr/bin/env python3
"""
This module provides a function to transpose a 2D matrix.
"""

def matrix_transpose(matrix):
    """Returns the transpose of a 2D matrix."""
    return [list(row) for row in zip(*matrix)]
