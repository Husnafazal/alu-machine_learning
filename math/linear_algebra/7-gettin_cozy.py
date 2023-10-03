#!/usr/bin/env python3
"""Concatenates two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Returns the concatenation of two 2D matrices along a given axis."""
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row.copy() for row in mat1] + [row.copy() for row in mat2]

    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [mat1[i].copy() + mat2[i].copy() for i in range(len(mat1))]

    return None
