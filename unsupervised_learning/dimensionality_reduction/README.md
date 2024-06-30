# Dimensionality Reduction Project

## Description

This project implements Principal Component Analysis (PCA) for dimensionality reduction.

## Files

- `0-pca.py`: Performs PCA to maintain a specified fraction of variance.
- `1-pca.py`: Performs PCA to transform data to a specified number of dimensions.
- `0-main.py`: Test script for `0-pca.py`.
- `1-main.py`: Test script for `1-pca.py`.
- `mnist2500_X.txt`: Dataset used for testing.

## Usage

To run the test scripts, use the following commands:

```bash
python3 0-main.py
python3 1-main.py

If you are using Visual Studio Code (VS Code), you can create and run the files directly within the editor. Below are the steps to set up and execute the code:

Create the Project Directory:
Create a new directory for your project, for example, dimensionality_reduction.

Create the Required Files:
Inside this directory, create the following Python files:

0-pca.py
python
Copy code
#!/usr/bin/env python3
import numpy as np

def pca(X, var=0.95):
    """Performs PCA on a dataset"""
    # Center the data
    X_centered = X - np.mean(X, axis=0)
    
    # Compute the covariance matrix
    covariance_matrix = np.cov(X_centered, rowvar=False)
    
    # Eigen decomposition
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)
    
    # Sort eigenvalues and eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    
    # Cumulative variance
    cumulative_variance = np.cumsum(sorted_eigenvalues) / np.sum(sorted_eigenvalues)
    
    # Select the number of components that maintain the specified variance
    num_components = np.searchsorted(cumulative_variance, var) + 1
    
    # Get the weight matrix
    W = sorted_eigenvectors[:, :num_components]
    
    return W
1-pca.py
python
Copy code
#!/usr/bin/env python3
import numpy as np

def pca(X, ndim):
    """Performs PCA on a dataset with fixed dimensionality"""
    # Center the data
    X_centered = X - np.mean(X, axis=0)
    
    # Compute the covariance matrix
    covariance_matrix = np.cov(X_centered, rowvar=False)
    
    # Eigen decomposition
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)
    
    # Sort eigenvalues and eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    
    # Select the top `ndim` eigenvectors
    W = sorted_eigenvectors[:, :ndim]
    
    # Transform the data
    T = np.dot(X_centered, W)
    
    return T
0-main.py
python
Copy code
#!/usr/bin/env python3

import numpy as np
pca = __import__('0-pca').pca

np.random.seed(0)
a = np.random.normal(size=50)
b = np.random.normal(size=50)
c = np.random.normal(size=50)
d = 2 * a
e = -5 * b
f = 10 * c

X = np.array([a, b, c, d, e, f]).T
m = X.shape[0]
X_m = X - np.mean(X, axis=0)
W = pca(X_m)
T = np.matmul(X_m, W)
print(T)
X_t = np.matmul(T, W.T)
print(np.sum(np.square(X_m - X_t)) / m)
1-main.py
python
Copy code
#!/usr/bin/env python3

import numpy as np
pca = __import__('1-pca').pca

X = np.loadtxt("mnist2500_X.txt")
print('X:', X.shape)
print(X)
T = pca(X, 50)
print('T:', T.shape)
print(T)
Data File
Make sure you have the data file mnist2500_X.txt in the same directory as the Python files.

Running the Code
Open VS Code and open your project directory.
Open a new terminal in VS Code by navigating to Terminal > New Terminal.
Run the test scripts using Python.
For 0-main.py:

bash
Copy code
python3 0-main.py
For 1-main.py:

bash
Copy code
python3 1-main.py
This will execute the scripts and you should see the output of the PCA transformations printed in the terminal.

Additional Tips
Ensure that you have the correct Python interpreter selected in VS Code. You can select the interpreter by clicking on the Python version in the bottom left corner of the VS Code window and selecting the appropriate Python 3 interpreter.
Make sure the data file mnist2500_X.txt is in the same directory as your Python scripts.
You can create a README.md file in your project directory to document your project.
README.md
markdown
Copy code
# Dimensionality Reduction Project

## Description

This project implements Principal Component Analysis (PCA) for dimensionality reduction.

## Files

- `0-pca.py`: Performs PCA to maintain a specified fraction of variance.
- `1-pca.py`: Performs PCA to transform data to a specified number of dimensions.
- `0-main.py`: Test script for `0-pca.py`.
- `1-main.py`: Test script for `1-pca.py`.
- `mnist2500_X.txt`: Dataset used for testing.

## Usage

To run the test scripts, use the following commands:

```bash
python3 0-main.py
python3 1-main.py
Requirements
Python 3
NumPy
arduino
Copy code

This setup should help you efficiently manage and run your project using Visual Studio Code.


