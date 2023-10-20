#!/usr/bin/env python3

"""
This module contains a method that performs convolution
on grayscale images with multiple kernels.
"""

import numpy as np

def convolve(images, kernels, padding='same', stride=(1, 1)):
    """
    Convolve grayscale images with multiple kernels.

    Args:
        images (numpy.ndarray): Input images with shape (m, h, w, c).
            m: Number of images.
            h: Height in pixels of the images.
            w: Width in pixels of the images.
            c: Number of channels in the images.
        kernels (numpy.ndarray): Convolution kernels with shape (kh, kw, kc, nc).
            kh: Height of the kernels.
            kw: Width of the kernels.
            kc: Number of channels in the kernels.
            nc: Number of kernels/filters.
        padding (str or tuple): Padding mode or tuple of padding values (
