#!/usr/bin/env python3
"""
sum of squared values
"""


def summation_i_squared(n):
    """ Sum i squared

    Args:
        n (_type_): _description_
    """
    if n == 1:
        return 1
    if n < 1:
        return None
    else:
        result = (n*(n+1)*(2*n+1))//6
        return result
