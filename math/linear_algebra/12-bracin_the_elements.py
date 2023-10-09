#!/usr/bin/env python3
"""
This module contains functions that perform element-wise operations on matrices.
"""


def np_elementwise(mat1, mat2):
    """
    Returns a tuple with element-wise addition, subtraction, multiplication, 
    and division of two matrices.
    """
    addition = mat1 + mat2
    subtraction = mat1 - mat2
    multiplication = mat1 * mat2
    division = mat1 / mat2
    return (addition, subtraction, multiplication, division)
