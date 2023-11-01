#!/usr/bin/env python3

"""
his component encompasses a technique that
carries out strided convolution operations on images in grayscale
"""
import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """
  Strided convolution operations applied to grayscale images.
    """
    # m, h, w = images.shape
    # kh, kw = kernel.shape

    # if padding == 'same':
    #     ph = max(0, (h - 1) * stride[0] + kh - h)
    #     pw = max(0, (w - 1) * stride[1] + kw - w)
    # elif isinstance(padding, tuple):
    #     ph, pw = padding
    # else:
    #     ph, pw = 0, 0

    # # stride
    # sh, sw = stride
    # # Calculate the output size with padding
    # out_h = (h + 2 * ph - kh) // sh + 1
    # out_w = (w + 2 * pw - kw) // sw + 1

    # padded_images = np.pad(
    #     images, ((0, 0), (ph, ph), (pw, pw)), mode='constant')
    # print(padded_images.shape)

    # # initialise convolved images
    # convolved_images = np.zeros((m, out_h, out_w))

    # for i in range(m):
    #     for j in range(out_h):
    #         for k in range(out_w):
    #             # Extract a patch from the image
    #             patch = padded_images[i, j * sh:j *
    #                                   sh + kh, k * sw:k * sw + kw]
    #             convolved_images[i, j, k] = np.sum(patch * kernel)
    #             print(convolved_images)

    # return convolved_images

    kh, kw = kernel.shape
    m, hm, wm = images.shape
    sh, sw = stride
    if padding == 'same':
        ph = int(((hm - 1) * sh + kh - hm) / 2) + 1
        pw = int(((wm - 1) * sw + kw - wm) / 2) + 1
    elif padding == 'valid':
        ph = 0
        pw = 0
    else:
        ph, pw = padding
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), 'constant')
    ch = int((hm + 2 * ph - kh) / sh) + 1
    cw = int((wm + 2 * pw - kw) / sw) + 1
    convoluted = np.zeros((m, ch, cw))
    for h in range(ch):
        for w in range(cw):
            square = padded[:, h * sh: h * sh + kh, w * sw: w * sw + kw]
            insert = np.sum(square * kernel, axis=1).sum(axis=1)
            convoluted[:, h, w] = insert
    return convoluted
