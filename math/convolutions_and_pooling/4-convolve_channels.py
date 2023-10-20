#!/usr/bin/env python3

"""
This module contains a method that performs
convolution on grayscale images with multiple channels.
"""


import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """
    Perform convolution on grayscale images with multiple channels.

    Args:
        images (numpy.ndarray): Input images with shape (m, h, w, c).
            m: Number of images.
            h: Height in pixels of the images.
            w: Width in pixels of the images.
            c: Number of channels in the images.
        kernel (numpy.ndarray): Convolution kernel with shape (kh, kw, kc).
            kh: Height of the kernel.
            kw: Width of the kernel.
            kc: Number of channels in the kernel.
        padding (str or tuple): Padding mode  (ph, pw).
            ph: Padding height.
            pw: Padding width.
            Options: 'same' (default), 'valid', or custom tuple.
        stride (tuple): Stride values (sh, sw) for the convolution operation.
            sh: Vertical stride.
            sw: Horizontal stride.
            Default: (1, 1).

    Returns:
        numpy.ndarray: Convolved images with shape (m, ch, cw).
            m: Number of images.
            ch: Height of the convolved images.
            cw: Width of the convolved images.
    """
    kh, kw, kc = kernel.shape
    m, hm, wm, cm = images.shape
    sh, sw = stride

    if padding == 'same':
        ph = int(((hm - 1) * sh + kh - hm) / 2) + 1
        pw = int(((wm - 1) * sw + kw - wm) / 2) + 1
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding

    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw), (0, 0)), 'constant')
    ch = int((hm + 2 * ph - kh) / sh) + 1
    cw = int((wm + 2 * pw - kw) / sw) + 1
    convoluted = np.zeros((m, ch, cw))
    for h in range(ch):
        for w in range(cw):
            square = padded[:, h * sh: h * sh + kh, w * sw: w * sw + kw, :]
            insert = np.sum(square * kernel, axis=1).sum(axis=1).sum(axis=1)
            convoluted[:, h, w] = insert
    return convoluted
