#!/usr/bin/env python3

def add_arrays(arr1, arr2):
    """Adds two arrays element-wise."""
    
    # Check if both arrays are of the same length
    if len(arr1) != len(arr2):
        return None
    
    # Return a new list containing the sum of elements at each index
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
