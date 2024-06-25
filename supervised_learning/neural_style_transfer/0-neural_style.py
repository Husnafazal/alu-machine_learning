import numpy as np
import tensorflow as tf

class NST:
    style_layers = [
        'block1_conv1', 'block2_conv1',
        'block3_conv1', 'block4_conv1', 'block5_conv1'
    ]
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e-2, beta=1e4):
        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta

    def scale_image(self, image):
        max_dim = 512
        long_dim = max(image.shape[:-1])
        scale = max_dim / long_dim
        new_shape = tf.cast(tf.shape(image)[:-1] * scale, tf.int32)
        image = tf.image.resize(image, new_shape)
        image = image[tf.newaxis, :]
        image = tf.clip_by_value(image / 255.0, 0.0, 1.0)
        return image
