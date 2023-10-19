#!/usr/bin/env python3

import numpy as np
from multinormal import MultiNormal

np.random.seed(0)
data = np.random.multivariate_normal([30, 40], [[75, 5], [5, 75]], 10000)
mean = np.mean(data, axis=0)
cov = np.cov(data, rowvar=False)

mn = MultiNormal(data)

# Make sure to reshape x into the right format
x = np.array([[1], [2]])
print(mn.pdf(x))
