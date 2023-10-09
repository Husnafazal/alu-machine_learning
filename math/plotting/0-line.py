#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# Plotting the data
plt.plot(y, 'r-')  # 'r-' means red color with solid line style

# Setting the x-axis limits
plt.xlim(0, 10)

# Displaying the plot
plt.show()
