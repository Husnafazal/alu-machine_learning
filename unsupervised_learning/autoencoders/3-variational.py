#!/usr/bin/env python3

"""This module creates a variational autoencoder."""

import tensorflow.keras as keras


def sampling(args):
    """Reparameterization trick by sampling from an isotropic unit Gaussian.

    Args:
        args (tensor): mean and log of variance of Q(z|X)

    Returns:
        z (tensor): sampled latent vector
    """
    z_mean, z_log_var = args
    batch = keras.backend.shape(z_mean)[0]
    dim = keras.backend.shape(z_mean)[1]
    epsilon = keras.backend.random_normal(shape=(batch, dim))
    return z_mean + keras.backend.exp(0.5 * z_log_var) * epsilon


def vae_loss(inputs, outputs, z_mean, z_log_var, input_dims):
    """Calculates the VAE loss which is the sum of reconstruction and KL divergence losses.

    Args:
        inputs (tensor): original input data
        outputs (tensor): reconstructed input data
        z_mean (tensor): mean of the latent variable
        z_log_var (tensor): log variance of the latent variable
        input_dims (int): dimensionality of the input data

    Returns:
        loss (tensor): VAE loss
    """
    reconstruction_loss = keras.losses.binary_crossentropy(inputs, outputs)
    reconstruction_loss *= input_dims
    kl_loss = 1 + z_log_var - keras.backend.square(z_mean) - keras.backend.exp(z_log_var)
    kl_loss = keras.backend.sum(kl_loss, axis=-1)
    kl_loss *= -0.5
    return keras.backend.mean(reconstruction_loss + kl_loss)


def autoencoder(input_dims, hidden_layers, latent_dims):
    """Creates a variational autoencoder (VAE).

    Args:
        input_dims (int): The dimension of the model input.
        hidden_layers (list): List containing the number of nodes for each hidden layer in the encoder,
                              reversed for the decoder.
        latent_dims (int): The dimension of the latent space representation.

    Returns:
        tuple: encoder, decoder, auto
            - encoder is the encoder model.
            - decoder is the decoder model.
            - auto is the full autoencoder model.
    """
    # Encoder
    inputs = keras.Input(shape=(input_dims,))
    x = inputs
    for nodes in hidden_layers:
        x = keras.layers.Dense(nodes, activation='relu')(x)
    z_mean = keras.layers.Dense(latent_dims)(x)
    z_log_var = keras.layers.Dense(latent_dims)(x)
    z = keras.layers.Lambda(sampling, output_shape=(latent_dims,), name='z')([z_mean, z_log_var])

    encoder = keras.Model(inputs, [z, z_mean, z_log_var], name='encoder')

    # Decoder
    latent_inputs = keras.Input(shape=(latent_dims,), name='z_sampling')
    x = latent_inputs
    for nodes in reversed(hidden_layers):
        x = keras.layers.Dense(nodes, activation='relu')(x)
    outputs = keras.layers.Dense(input_dims, activation='sigmoid')(x)

    decoder = keras.Model(latent_inputs, outputs, name='decoder')

    # VAE Model
    outputs = decoder(encoder(inputs)[0])
    auto = keras.Model(inputs, outputs, name='vae')

    # Add the loss as a layer
    class VAELossLayer(keras.layers.Layer):
        """Custom layer to add VAE loss."""
        def call(self, inputs):
            inputs, outputs, z_mean, z_log_var = inputs
            loss = vae_loss(inputs, outputs, z_mean, z_log_var, input_dims)
            self.add_loss(loss)
            return outputs

    outputs = VAELossLayer()([inputs, outputs, encoder(inputs)[1], encoder(inputs)[2]])
    auto = keras.Model(inputs, outputs, name='vae')
    auto.compile(optimizer='adam')

    return encoder, decoder, auto
