#!/usr/bin/env python3
"""
Defines a function that calculates the accuracy of a prediction
for the neural network
"""


import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """
     Determines the match accuracy between the neural network's predictions and the actual labels

    Parameters:
        y_true [tf.placeholder]: a placeholder for the actual labels of the input data
        y_predicted [tensor]: encapsulates the predictions made by the network
        
    returns:
        A tensor that represents the prediction's accuracy as a decimal value
    """
    y_pred = tf.math.argmax(y_pred, axis=1)
    y = tf.math.argmax(y, axis=1)
    equality = tf.math.equal(y_pred, y)
    accuracy = tf.reduce_mean(tf.cast(equality, "float"))
    return accuracy
