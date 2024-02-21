#!/usr/bin/env python3

"""Module with a function to compute
softmax cross-entropy loss for
model predictions"""

import tensorflow as tf

def compute_loss(y_true, y_estimate):
    """
    y_true - placeholder for the true labels of the input data
    y_estimate - tensor representing the model's predictions
    Outputs a tensor with the calculated prediction loss
    """
    # Conversion of y_estimate to categorical labels was considered but not used
    # actual_labels = tf.argmax(y_true, 1)
    # estimated_labels = tf.argmax(y_estimate, 1)

    loss = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(
            labels=y_true, logits=y_estimate), name="softmax_cross_entropy_loss/value")

    return loss
