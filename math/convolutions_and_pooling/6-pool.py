#!/usr/bin/env python3

"""
This module contains a method
sthat performs pooling on images.
"""

import numpy as np

def pool(images, kernel_shape, stride, mode='max'):
    """
    Apply pooling on images.

    Args:
        images (numpy.ndarray): Input images with shape (m, h, w, c).
            m: Number of images.
            h: Height in pixels of the images.
            w: Width in pixels of the images.
            c: Number of channels in the images.
        kernel_shape (tuple): Pooling kernel shape (kh, kw).
            kh: Height of the pooling kernel.
            kw: Width of the pooling kernel.
        stride (tuple): Stride values (sh, sw) for the pooling operation.
            sh: Vertical stride.
            sw: Horizontal stride.
        mode (str): Pooling mode, either 'max' (default) or 'avg'.

    Returns:
        numpy.ndarray: Pooled images with shape (m, oh, ow, c).
            m: Number of images.
            oh: Height of the pooled images.
            ow: Width of the pooled images.
            c: Number of channels in the images.
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    # Calculate the output dimensions
    oh = int((h - kh) / sh) + 1
    ow = int((w - kw) / sw) + 1

    # Initialize the output tensor
    pooled_images = np.zeros((m, oh, ow, c))

    for i in range(oh):
        for j in range(ow):
            # Extract a patch from the image
            patch = images[:, i * sh:i * sh + kh, j * sw:j * sw + kw, :]

            # Apply pooling based on the specified mode
            if mode == 'max':
                pooled_patch = np.max(patch, axis=(1, 2))
            elif mode == 'avg':
                pooled_patch = np.mean(patch, axis=(1, 2))
            else:
                raise ValueError("Invalid pooling mode. Use 'max' or 'avg'.")

            # Store the pooled patch in the output
            pooled_images[:, i, j, :] = pooled_patch

    return pooled_images
