import matplotlib.pyplot as mp
import numpy as np

# Generate linearly spaced data points between 1 and 10
x = np.linspace(1, 10, 200)
print(x)

# Compute the sine of each data point
y = np.sin(x)
print(y)

# Plot the sine wave with a dashed blue line
mp.plot(x, y, "--b")

# Uncomment the following lines to add labels and title to the plot
# mp.xlabel("X-axis: Data Points")
# mp.ylabel("Y-axis: Sine Values")
# mp.title("Sine Wave Plot")
# mp.grid(True)  # Add grid lines to the plot
# mp.figure(figsize=(10, 6))  # Set the figure size

# Generate random data for scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
colours = np.random.rand(50)  # Random colors for each point
size = 1000 * np.random.rand(50)  # Random sizes for each point

print(x)
print(y)

# Create a scatter plot with default settings
mp.scatter(x, y)

# Create a scatter plot with colors
mp.scatter(x, y, c=colours, alpha=0.5)  # Set alpha for color intensity

# Generate data for bar graph
x = ["a", "b", "c"]
y = np.random.rand(3)

# Create a vertical bar graph
mp.bar(x, y)
print(y)

# Create a horizontal bar graph
mp.barh(x, y)
print(y)

# Generate data for line plot
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 4]

# Plot the line graph
mp.plot(x, y)

# Display all plots
mp.show()

# Generate data for histogram
data = [1, 2, 3, 4, 5, 1, 2, 3, 6, 7]

# Create a histogram
mp.hist(data)

# Display the histogram
mp.show()

# Uncomment the following lines to create a 3D plot
# fig = mp.figure()
# ax = fig.add_subplot(111, projection='3d')
