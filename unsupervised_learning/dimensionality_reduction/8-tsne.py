def tsne(X, ndims=2, idims=50, perplexity=30.0, iterations=1000, lr=500):
    """
    Performs a t-SNE transformation

    parameters:
        X [numpy.ndarray of shape (n, d)]:
            containing the dataset to be transformed by t-SNE
            n: the number of data points
            d: the number of dimensions in each point
        ndims [int]:
            the new dimensional representation of X
        idims [int]:
            the intermediate dimensional representation of X after PCA
        perplexity [float]:
            perplexity that all Gaussian distributions should have
        iterations [int]:
            the number of iterations
        lr [float]:
            the learning rate

    returns:
        Y [numpy.ndarray of shape (n, ndims)]:
            containing the optimized low dimensional transformation of X
    """
    # Step 1: Perform PCA to reduce dimensionality
    X_pca = pca(X, idims)

    # Step 2: Compute P affinities
    P = P_affinities(X_pca, perplexity)

    # Step 3: Gradient descent optimization
    Y = np.random.normal(0, 0.1, size=(X.shape[0], ndims))  # Initialize Y randomly

    for i in range(iterations):
        Y, grads, cost_i = grads(Y, P)
        if i % 100 == 0:
            print(f"Cost at iteration {i}: {cost_i}")

        # Update Y using gradient descent with learning rate lr

    return Y
