#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

# Plotting the data as line graphs
plt.plot(x, y1, 'r--', label='C-14')  # Dashed red line for y1
plt.plot(x, y2, 'g-', label='Ra-226')  # Solid green line for y2

# Setting the labels, title, and other specifications
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of Radioactive Elements')
plt.xlim(0, 20000)  # Setting the x-axis range from 0 to 20,000
plt.ylim(0, 1)      # Setting the y-axis range from 0 to 1

# Displaying the legend in the upper right corner
plt.legend(loc='upper right')

# Displaying the plot
plt.show()
