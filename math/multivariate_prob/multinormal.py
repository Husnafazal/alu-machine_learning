import numpy as np

class MultiNormal:
    def __init__(self, data):
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        if data.shape[1] < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1).reshape(-1, 1)
        self.cov = np.dot(data - self.mean, (data - self.mean).T) / (data.shape[1] - 1)

    def pdf(self, x):
        if not isinstance(x, np.ndarray):
            raise ValueError("x must be a numpy.ndarray")
        if x.shape != (self.mean.shape[0], 1):
            raise ValueError(f"x must have the shape ({self.mean.shape[0]}, 1)")

        d = self.mean.shape[0]
        det = np.linalg.det(self.cov)
        inv_cov = np.linalg.inv(self.cov)
        diff = x - self.mean
        exponent = -0.5 * np.dot(np.dot(diff.T, inv_cov), diff)
        prefactor = 1 / (np.sqrt((2 * np.pi) ** d * det))

        return prefactor * np.exp(exponent)
