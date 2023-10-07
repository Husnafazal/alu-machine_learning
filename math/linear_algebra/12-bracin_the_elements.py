#!/usr/bin/env python3
"""
This module contains functions that perform element-wise operations on matrices.
"""

import numpy as np

def np_elementwise(mat1, mat2):
    """
    Returns a tuple with element-wise addition, subtraction, multiplication, 
    and division of two matrices.
    """
    addition = np.add(mat1, mat2)
    subtraction = np.subtract(mat1, mat2)
    multiplication = np.multiply(mat1, mat2)
    division = np.divide(mat1, mat2)
    return (addition, subtraction, multiplication, division)
