import numpy as np
from bayes_opt import BayesianOptimization

# Define the black-box function to be optimized
def black_box_function(x):
    return -1 * (x ** 2)

# Initial samples (inputs and their corresponding outputs)
X_init = np.array([[2.0], [3.0], [4.0]])
Y_init = black_box_function(X_init)

# Define bounds of the search space
bounds = (0, 5)
# Number of samples to evaluate during acquisition
ac_samples = 50

# Initialize Bayesian Optimization with the initial samples and bounds
bayes_opt = BayesianOptimization(
    f=black_box_function,
    X_init=X_init,
    Y_init=Y_init,
    bounds=bounds,
    ac_samples=ac_samples
)

# Perform optimization for a specified number of iterations
optimal_x, optimal_y = bayes_opt.optimize(iterations=10)

print(f"Optimal x: {optimal_x}")
print(f"Optimal y: {optimal_y}")
