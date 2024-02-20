#!/usr/bin/env python3

"""This module contains a function that
returns tensor output of the layer and defines neural networks """

import tensorflow as tf


def create_layer(prev, n, activation):
    """
    n - the number of nodes in the layer to be created; prior -
    the tensor output of the previous layer
    layer - layer names; activation - activation function;
    """
    # He et al. initializer for the layer weights
    initializer = tf.contrib.layers.variance_scaling_initializer(
        mode="FAN_AVG")

    # Create the layer
    layer = tf.layers.dense(inputs=prev,
                            units=n,
                            activation=activation,
                            kernel_initializer=initializer,
                            name='layer')
    return layer
