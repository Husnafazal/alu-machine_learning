#!/usr/bin/env python3

"""
This module contains a method that performs a valid
convolution on grayscale images with "same" padding.
"""

import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    Perform a valid convolution on grayscale images with "same" padding.

    Args:
        images (numpy.ndarray): Input images with shape (m, h, w).
            m: Number of images.
            h: Height in pixels of the images.
            w: Width in pixels of the images.
        kernel (numpy.ndarray): Convolution kernel with shape (kh, kw).
            kh: Height of the kernel.
            kw: Width of the kernel.

    Returns:
        numpy.ndarray: Convolved images with shape (m, hm, wm).
            m: Number of images.
            hm: Height of the convolved images.
            wm: Width of the convolved images.
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    m, h, w = images.shape
    kh, kw = kernel.shape

    # Calculate the padding required to maintain the same output size
    # padding_h = kh // 2
    # padding_w = kw // 2
    # padded_images = np.pad(
    #     images, ((0, 0), (padding_h, padding_h), (padding_w, padding_w)),
    #     mode='constant')

    # Perform convolution
    # convolved_images = np.zeros((m, h, w))
    # for i in range(m):
    #     for j in range(h):
    #         for k in range(w):
    #             patch = padded_images[i, j:j + kh, k:k + kw]
    #             convolved_images[i, j, k] = np.sum(patch * kernel)
    #             print(convolved_images)

    # return convolved_images

    kh, kw = kernel.shape
    m, hm, wm = images.shape
    ph = int(kh / 2)
    pw = int(kw / 2)
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), 'constant')
    convoluted = np.zeros((m, hm, wm))
    for h in range(hm):
        for w in range(wm):
            square = padded[:, h: h + kh, w: w + kw]
            insert = np.sum(square * kernel, axis=1).sum(axis=1)
            convoluted[:, h, w] = insert
    return convoluted
