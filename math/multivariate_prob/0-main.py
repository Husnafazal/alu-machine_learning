#!/usr/bin/env python3

import numpy as np
from multinormal import MultiNormal

if __name__ == "__main__":
    data = np.load('data.npy')
    mean = np.array([12, 30, 10])
    cov = np.array([[36, -30, 15], [-30, 100, -20], [15, -20, 25]])
    mn = MultiNormal(mean, cov)
    
    # Convert your input to numpy array before passing it to the pdf method
    x_input = np.array([[1, 2, 3, 4, 5]])
    print(mn.pdf(x_input))
