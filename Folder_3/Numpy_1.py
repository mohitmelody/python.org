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
arr9 = np.zeros((3,4))
# second dimension 
print(arr9)
arr10= np.zeros((3, 4 ,4))
#  third dimension 
print(arr10)


arr = np.ones((2, 3))
print(arr)


arr = np.ones((2, 3, 2))
print(arr)


print(arr *4)

# empty array create kar rahe hain 
arr = np.empty((2, 2), dtype=int)
print(arr)

# identity marix in numpy
np.eye(3,2)

# logspaces
np.logspace(3,2 , 10)
np.logspace(3, 2 , base= 2)

# function used in AI 
arr11 = np.random.randn(3,4)
# generate that data which mean is 0 and standard deviation is 1
print(arr11)
import pandas as pd
import csv
print(pd.DataFrame(arr11))

arr12 = np.random.rand(3,4)
print(arr12)
arr13 =  np.random.randint(1, 1111 , (300, 400))
# print(pd.DataFrame(arr13)).to_csv("text.csv")

# reshape your data 
print(arr12.reshape(6,2))
print(arr12[0][1])

