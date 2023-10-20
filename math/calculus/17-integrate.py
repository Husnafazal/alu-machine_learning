#!/usr/bin/env python3
""" 
calculates the integral
"""


def poly_integral(poly, C=0):
    """ Calculate integral of a polynomial. """
    if not all(isinstance(c, (int, float)) for c in poly) or not isinstance(C, int):
        return None
    
    integral = [C] + [coef / (i + 1) for i, coef in enumerate(poly)]
    while integral[-1] == 0 and len(integral) > 1: integral.pop()
    return [int(c) if c.is_integer() else c for c in integral]

if __name__ == "__main__":
    print(poly_integral([5, 3, 0, 1]))
