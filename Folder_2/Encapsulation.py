# Encapsulation

# Define a class named 'datScience'
# Encapsulation is used to protect the data from modification by external code, user
class datScience:
    # Initialize the class with two private attributes
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    # Define a setter method for attribute 'a'
    def set_a(self, a):
        self.__a = a

    # Define a setter method for attribute 'b'
    def set_b(self, b):
        self.__b = b

    # Define a method to get the values of the attributes
    def get_value(self):
        return self.__a, self.__b

# Create an instance of 'datScience' with initial values 1 and 2
data = datScience(23, 34)
print(data.get_value())
data.__b = 112
print(datScience)
# Access and modify the private attribute '__b' directly (not recommended)
# data._datScience__b = 24
# Print the modified value of '__b'
print(data._datScience__b)  # Output: 24

# Use the setter method to set the value of 'b' to 24
data.set_b(24)
# Use the setter method to set the value of 'a' to 24
data.set_a(24)

# Use the getter method to get the values of 'a' and 'b'
print(data.get_value())  # Output: (24, 24)
