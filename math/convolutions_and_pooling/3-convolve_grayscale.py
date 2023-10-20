#!/usr/bin/env python3

"""
This module contains a method that performs 
convolution on grayscale images with padding.
"""


import numpy as np

def convolve_grayscale_padding(images, kernel, padding):
    """
    Perform convolution on grayscale images with specified padding.

    Args:
        images (numpy.ndarray): Input grayscale images with shape (m, h, w).
            m: Number of images.
            h: Height in pixels of the images.
            w: Width in pixels of the images.
        kernel (numpy.ndarray): Convolution kernel with shape (kh, kw).
            kh: Height of the kernel.
            kw: Width of the kernel.
        padding (tuple): Tuple containing padding values (ph, pw).
            ph: Padding height.
            pw: Padding width.

    Returns:
        numpy.ndarray: Convolved images with shape (m, ch, cw).
            m: Number of images.
            ch: Height of the convolved images.
            cw: Width of the convolved images.
    """
    kh, kw = kernel.shape
    m, hm, wm = images.shape
    ph, pw = padding
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), 'constant')
    ch = hm + (2 * ph) - kh + 1
    cw = wm + (2 * pw) - kw + 1
    convoluted = np.zeros((m, ch, cw))
    for h in range(ch):
        for w in range(cw):
            square = padded[:, h: h + kh, w: w + kw]
            insert = np.sum(square * kernel, axis=1).sum(axis=1)
            convoluted[:, h, w] = insert
    return convoluted
