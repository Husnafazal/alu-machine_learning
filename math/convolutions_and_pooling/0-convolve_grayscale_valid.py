#!/usr/bin/env python3

"""
This module contains a method that performs a valid
convolution on grayscale images.
"""

import numpy as np

def convolve_grayscale_valid(images, kernel):
    """
    Perform a valid convolution on grayscale images.

    Args:
        images (numpy.ndarray): Input images with shape (m, h, w).
            m: Number of images.
            h: Height in pixels of the images.
            w: Width in pixels of the images.
        kernel (numpy.ndarray): Convolution kernel with shape (kh, kw).
            kh: Height of the kernel.
            kw: Width of the kernel.

    Returns:
        numpy.ndarray: Convolved images with shape (m, output_h, output_w).
            output_h: Height of the convolved images.
            output_w: Width of the convolved images.
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    output_h = h - kh + 1
    output_w = w - kw + 1
    output = np.zeros((m, output_h, output_w))
    for i in range(output_h):
        for j in range(output_w):
            output[:, i, j] = (kernel * images[:, i: i + kh, j: j + kw])\
                .sum(axis=(1, 2))
    return output
