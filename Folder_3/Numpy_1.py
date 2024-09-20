# Solving numerical problems in Python using these libraries

# Data processing
# Data is passed in arrays and matrices
# At the end, the system converts the data into arrays
# NumPy deals with arrays and matrices

# NumPy ndarray
# In computation, arrays can be 1-dimensional or 2-dimensional
# Python creates ndarrays to represent these array dimensions
# An ndarray is a multi-dimensional array of items of the same type and size


# Solving numerical problems in Python using these libraries

# Importing numpy for array and matrix operations
import pandas as pd
import numpy as np

# Creating a list
l = [1, 2, 3]

# Converting list to numpy array
arr = np.array(l)
print(type(arr))  # Output: <class 'numpy.ndarray'>

# Example of a one-dimensional array
one_d_array = np.array([1, 2, 3])

# Example of a two-dimensional array
two_d_array = np.array([[1, 2, 3],
                        [4, 5, 6]])

# Converting list to array using asarray and asanyarray
print(np.asarray(l))
print(np.asanyarray(l))

# Creating a matrix from a list
# Note: numpy.matrix is strictly 2-dimensional
matrix = np.matrix(l)
print(matrix)

# Demonstrating shallow copy
b = l
print(np.asanyarray(b))
print(np.asarray(b))

# Demonstrating deep copy
d = np.copy(l)
print(d)
b[0] = 342
print(l)  # Original list modified
print(d)  # Deep copy remains unchanged

# Using fromfunction to create arrays with specific patterns
state = np.fromfunction(lambda i, j: i == j, (3, 4))
print(state)

state = np.fromfunction(lambda i, j: i * j, (3, 4))
print(state)

state = np.fromfunction(lambda i, j: i + j, (3, 4))
print(state)

state = np.fromfunction(lambda i, j: i - j, (3, 4))
print(state)

# Creating array from string
state1 = "3,4,5"
print(np.fromstring(state1, sep=","))

# Creating array from an iterable
state3 = (i * i for i in range(6))
print(np.fromiter(state3, float))


# 55
#  check datatype in nu
# Create an array of integers
array1 = np.array([6, 7, 8])
print(array1.dtype)  # Output: int64

# Create an array of floats
array2 = np.array([1.1, 2.2, 3.3])
print(array2.dtype)  # Output: float64

# check size
# Create a 2x3 array
array3 = np.array([[1, 2, 3], [4, 5, 6]])
print(array3.size)  # Output: 6

# Create a 1D array
array4 = np.array([1, 2, 3])
print(array4.ndim)  # Output: 1

# create a 2D array
arr2 = np.array([[1, 2], [3, 4]])
print(arr2.ndim)
# Create a 3D array
array5 = np.zeros((2, 3, 4))
print(array5.ndim)  # Output: 3

# Create a 2D array
array1 = np.array([[1, 2, 3], [4, 5, 6]])
print(array1.shape)  # Output: (2, 3)

# Create a 3D array
array2 = np.zeros((3, 4, 5))
print(array2.shape)  # Output: (3, 4, 5)


# Create an array with values from 0 to 9
array1 = np.arange(10)
print(array1)  # Output: [0 1 2 3 4 5 6 7 8 9]

# Create an array with values from 1 to 9
array2 = np.arange(1, 10)
print(array2)  # Output: [1 2 3 4 5 6 7 8 9]

# Create an array with values from 1 to 9 with a step of 2
array3 = np.arange(1, 10, 2)
print(array3)  # Output: [1 3 5 7 9]

# Create an array with floating point values
array4 = np.arange(0, 1, 0.1)
print(array4)  # Output: [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]

ran = np.arange(2.3, 4.4)
print(ran)


# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Convert the array to a list
list_from_array = array.tolist()

print(list_from_array)  # Output: [1, 2, 3, 4, 5]

#  line spaces is a  Data generator function
linespaces = np.linspace(1, 8, 12)
print(linespaces)

arr8 = np.zeros(5)
# one dimension
print(arr8)
arr9 = np.zeros((3, 4))
# second dimension
print(arr9)
arr10 = np.zeros((3, 4, 4))
#  third dimension
print(arr10)


# Create a 2x3 array filled with ones
arr = np.ones((2, 3))
print(arr)

# Create a 2x3x2 array filled with ones
arr = np.ones((2, 3, 2))
print(arr)

# Multiply the array by 4
print(arr * 4)

# Create an empty 2x2 array with integer type
arr = np.empty((2, 2), dtype=int)
print(arr)

# Create a 3x2 identity matrix
print(np.eye(3, 2))

# Generate 10 numbers between 10^3 and 10^2
print(np.logspace(3, 2, 10))

# Generate 10 numbers between 2^3 and 2^2
print(np.logspace(3, 2, 10, base=2))

# Generate a 3x4 array with random numbers from a normal distribution
arr11 = np.random.randn(3, 4)
# The data has a mean of 0 and standard deviation of 1
print(arr11)

# Convert the array to a DataFrame for better visualization
print(pd.DataFrame(arr11))

# Generate a 3x4 array with random numbers between 0 and 1
arr12 = np.random.rand(3, 4)
print(arr12)

# Generate a 300x400 array with random integers between 1 and 1110
arr13 = np.random.randint(1, 1111, (300, 400))
# Save the array to a CSV file (commented out)
# print(pd.DataFrame(arr13)).to_csv("text.csv")

# Reshape the 3x4 array to a 6x2 array
print(arr12.reshape(6, 2))

# Access the element at row 0, column 1
print(arr12[0][1])

# Generate a 5x5 array with random integers between 1 and 99
arr14 = np.random.randint(1, 100, (5, 5))
print(arr14)

# Print a boolean array where elements are greater than 50
print(arr14 > 50)

# Print elements of the array that are greater than 50
print(arr14[arr14 > 50])

# Access a subarray from row 2 to 3 and columns 1 and 2
print(arr14[2:4, [1, 2]])

# Access the element at row 0, column 0
print(arr14[0][0])

# Add two arrays (commented out)
# print(arr13 + arr14)
# Check if the dimensions are the same

# Generate two matrices for multiplication
mat1 = np.random.randint(1, 50, (3, 4))
mat2 = np.random.randint(50, 100, (4, 3))
print(mat1)
print(mat2)

# Matrix multiplication using @ operator
print(mat1 @ mat2)

# Division by zero (will raise an error)
print(mat1 / 0)

# Add 100 to each element of the matrix
print(mat1 + 100)

# Square each element of the matrix
print(mat1 ** 2)

# Create a 4x3 array filled with zeros
mat5 = np.zeros((4, 3))
print(mat5)

# Create a 1D array
zrr16 = np.array([1, 2, 3])

# Row-wise broadcasting
print(mat5 + zrr16)

# Create a 2D array and transpose it
zrr18 = np.array([[1, 2, 3]])
print(zrr18.T)

# Broadcasting with a 2D array
print(mat5 + zrr18)

# Apply square root to each element of the matrix
print(np.sqrt(mat1))

# Apply exponential function to each element of the matrix
print(np.exp(mat1))

# Apply natural logarithm to each element of the matrix
print(np.log(mat1))

# convert two dimensional array into one dimensional by flatten
print(mat1.flatten())

# Original array
x = np.array([1, 2, 3])
z = np.expand_dims(x, axis=0)
# 0 rows
print(x.ndim)
# print("Original array shape:", x)

# Expanding dimensions
y = np.expand_dims(x, axis=1)

print(y)
print(x.ndim)


x = np.array([[[0], [1], [2]]])
print("Original array shape:", x.shape)

# Squeezing the array
y = np.squeeze(x)
print("Squeezed array shape:", y.shape)
print(y)

# also having a repeat

arr21 = np.repeat(x, 3)
print(arr21)

arr22 = np.roll(x, 2)
print(arr22)

# diagonally
# arr23 = np.diag(x)
# print(arr23)
# binary opertaions
mat5 = np.random.randint(1, 50, (3, 4))
mat6 = np.random.randint(50, 100, (3, 4))
print(mat5 + mat6)
print(mat5 * mat6)
print(mat6 - mat5)
print(mat5 / mat6)
print(mat5 | mat6)
print(mat5 > mat6)
print(~ mat6)


# numpy string functions
str_arr = np.array(["mohit", "developers"])
print(str_arr)
str_arr2 = np.char.upper(str_arr)
print(str_arr2)
str_arr3 = np.char.title(str_arr)
str_arr24 = np.char.capitalize(str_arr)
print(str_arr24)
print(str_arr3)

print(np.sin(mat1))
print(np.cos(mat1))
print(np.tan(mat1))
print(np.log10(mat1))
print(np.min(mat1))
print(np.max(mat1))
print(np.var(mat1))
print(np.mean(mat1))
print(np.std(mat1))
