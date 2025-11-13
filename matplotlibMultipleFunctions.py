# Unit 2 Question 3 part 3

# Objectives:
# Initialize a line plot using matplotlib
# Create a plot of a tan function with names for the plot title, x-axis, and y-axis of your choice
# Create a plot with a tan and cos function with names for the plot title, x-axis, and y-axis of your choice
# For both plots, ensure the x-axis has equal spacing from 0 to 2pi using 50 samples
# Make sure both plots have a grid enabled

import math
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*math.pi, 50)
y1 = np.tan(x)
y2 = np.cos(x)

# enable grid 
plt.grid(True)

# Customize appearance
plt.plot(x, y1, color='red')
plt.plot(x, y2, color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('tan(x) and cos(x)')

plt.show()