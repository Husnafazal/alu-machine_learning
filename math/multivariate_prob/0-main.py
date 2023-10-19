#!/usr/bin/env python3

import numpy as np
from multinormal import MultiNormal

mn = MultiNormal(...)
x_list = [[1, 2, 3, 4, 5]]
x_array = np.array(x_list)

result = mn.pdf(x_array)
print(result)
