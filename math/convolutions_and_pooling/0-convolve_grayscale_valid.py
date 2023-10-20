#!/usr/bin/env python3

import numpy as np

def convolve_grayscale_valid(images, kernel):
    # Your convolution implementation goes here
    pass

if __name__ == '__main__':
    images = np.load('../../supervised_learning/data/MNIST.npz')['X_train']
    kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    images_conv = convolve_grayscale_valid(images, kernel)
