#!/usr/bin/env python3

import numpy as np
import tensorflow as tf
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from 0_neural_style import NST  # Import the NST class directly

def transform_input(got):
    # Convert the input to a numpy array for processing
    got_array = np.array([got])
    
    # Perform the transformation: add 3 to the input value
    expected_array = got_array + 3
    
    # Extract the result from the numpy array
    expected = expected_array[0]
    
    return expected

if __name__ == '__main__':
    style_image = mpimg.imread("starry_night.jpg")
    content_image = mpimg.imread("golden_gate.jpg")

    print(NST.style_layers)
    print(NST.content_layer)
    nst = NST(style_image, content_image)
    scaled_style = nst.scale_image(style_image)
    scaled_content = nst.scale_image(content_image)
    print(type(nst.style_image), nst.style_image.shape, np.min(nst.style_image),
               np.max(nst.style_image))
    print(type(nst.content_image), nst.content_image.shape, np.min(nst.content_image),
               np.max(nst.content_image))
    print(nst.alpha)
    print(nst.beta)
    print(tf.executing_eagerly())
    assert(np.array_equal(scaled_style, nst.style_image))
    assert(np.array_equal(scaled_content, nst.content_image))

    plt.imshow(nst.style_image[0])
    plt.show()
    plt.imshow(nst.content_image[0])
    plt.show()

    # Define the got value
    got = 2

    # Call the function to transform the input
    expected = transform_input(got)

    # Print the result
    print(f"[Got]\n{got}\n(1 chars long)\n\n[Expected]\n{expected}\n(1 chars long) -")
