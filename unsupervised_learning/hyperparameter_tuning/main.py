#!/usr/bin/env python
import numpy as np
from bayes_opt import BayesianOptimization

# Define the function you want to optimize (example)
def black_box_function(x, y):
    return -x ** 2 - (y - 1) ** 2 + 1

# Define the bounds of the input variables
pbounds = {'x': (-4, 4), 'y': (-3, 3)}

# Create the optimizer object with your function and bounds
optimizer = BayesianOptimization(
    f=black_box_function,
    pbounds=pbounds,
    random_state=1,  # Random seed for reproducibility
)

# Perform optimization
optimizer.maximize(init_points=2, n_iter=5)

# Print the best result
print(optimizer.max)
