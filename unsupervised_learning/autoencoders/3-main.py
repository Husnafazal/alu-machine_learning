#!/usr/bin/env python3
"""
Module that defines a variational autoencoder (VAE)
"""

import tensorflow.keras as keras
from keras import layers, models, backend as K
from keras.losses import binary_crossentropy

def sampling(args):
    """Reparameterization trick by sampling from an isotropic unit Gaussian.
    Arguments:
        args (tensor): mean and log of variance of Q(z|X)
    Returns:
        z (tensor): sampled latent vector
    """
    z_mean, z_log_var = args
    batch = K.shape(z_mean)[0]
    dim = K.int_shape(z_mean)[1]
    epsilon = K.random_normal(shape=(batch, dim))
    return z_mean + K.exp(0.5 * z_log_var) * epsilon

def autoencoder(input_dims, hidden_layers, latent_dims):
    """Creates a variational autoencoder.
    
    Arguments:
        input_dims (int): dimensions of the model input
        hidden_layers (list): number of nodes for each hidden layer in the encoder
        latent_dims (int): dimensions of the latent space representation
    
    Returns:
        encoder (Model): encoder model
        decoder (Model): decoder model
        auto (Model): full autoencoder model
    """
    # Encoder
    inputs = keras.Input(shape=(input_dims,))
    x = inputs
    for units in hidden_layers:
        x = layers.Dense(units, activation='relu')(x)
    
    z_mean = layers.Dense(latent_dims)(x)
    z_log_var = layers.Dense(latent_dims)(x)
    
    z = layers.Lambda(sampling, output_shape=(latent_dims,))([z_mean, z_log_var])
    
    encoder = models.Model(inputs, [z, z_mean, z_log_var], name='encoder')
    
    # Decoder
    latent_inputs = keras.Input(shape=(latent_dims,))
    x = latent_inputs
    for units in reversed(hidden_layers):
        x = layers.Dense(units, activation='relu')(x)
    outputs = layers.Dense(input_dims, activation='sigmoid')(x)
    
    decoder = models.Model(latent_inputs, outputs, name='decoder')
    
    # Autoencoder
    outputs = decoder(encoder(inputs)[0])
    auto = models.Model(inputs, outputs, name='autoencoder')
    
    # Loss function
    reconstruction_loss = binary_crossentropy(inputs, outputs) * input_dims
    kl_loss = -0.5 * K.sum(1 + z_log_var - K.square(z_mean) - K.exp(z_log_var), axis=-1)
    vae_loss = K.mean(reconstruction_loss + kl_loss)
    auto.add_loss(vae_loss)
    
    auto.compile(optimizer='adam')
    
    return encoder, decoder, auto
