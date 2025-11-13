# Unit 2 Question 3 Part 1

import matplotlib.pyplot as plt

# Sample dataset (time points and brightness measurements)
time_points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Time points
brightness = [10, 10, 30, 80, 140, 120, 100, 80, 60, 30, 10]  # Brightness measurements

# Customize appearance
plt.plot(time_points, brightness, color='purple', linestyle='--', marker='o', markersize=5)
plt.xlabel('Time')
plt.ylabel('Brightness')
plt.title('Brightness of Supernova')

# Show plot
plt.show()