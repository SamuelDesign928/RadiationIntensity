import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Sample data
x = [3, 6, 9, 12, 15, 18, 21, 24]
y = [0.224, 0.225, 0.394, 0.514, 0.640, 0.788, 0.864, 1.07]

# Calculate the line of best fit
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Create a scatter plot
plt.scatter(x, y, label="Data Points")

# Create a line of best fit using the calculated slope and intercept
line_of_best_fit = [(slope * xi) + intercept for xi in x]

# Extend the x-axis to include negative values and extrapolation
x_extended = np.linspace(min(x) - 5, max(x) + 5, 100)

# Calculate the corresponding y-values for the extended x-axis
y_extended = [(slope * xi) + intercept for xi in x_extended]

# Plot the line of best fit with extended x-axis
plt.plot(x_extended, y_extended, color="red", label="Line of Best Fit")

# Add labels and a legend
plt.xlabel("Distance (cm)")
plt.ylabel("1/√Cc (Bq)")
plt.title("A graph to show the intensity of gamma radiation")  # Title of the graph
plt.legend()

# Annotate the plot with the gradient (slope)
gradient_text = f'Gradient (Slope): {slope:.2f}'
plt.annotate(gradient_text, xy=(10, 2), fontsize=12, color='blue')

# Show the plot
plt.grid(True)
plt.show()
