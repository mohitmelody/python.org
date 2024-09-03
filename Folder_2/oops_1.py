# Initialize a variable with an integer value
a = 1
# Print the type of the variable 'a'
print(type(a))  # Output: <class 'int'>

# About class
# A class is basically a real-world entity that indicates what it represents.
# For example, if we talk about the class 'int', it represents integer values.
# A class is a blueprint or skeleton.
# A class is a blueprint of an object.

# About object
# The real-world entity is an object.
# An object or attributes are instances of a class.
# For example, 'int', 'list', etc.
# An object belongs to a class.

# How to declare your own class
# A class provides structure and classification of code.
# The class written can be imported and used to access variables and methods.
# Open source helps in this regard.

# Define a simple class named 'test'
class test:
    pass

# Create an instance of the 'test' class
a = test()
# Print the type of the instance 'a'
print(type(a))  # Output: <class '__main__.test'>

# Define a class named 'mohitSkils'
class mohitSkils:
    # The 'self' keyword is used to bind and connect the class and its methods
    def myskills(self):
        print("hello")

# Create an instance of 'mohitSkils' and call the 'myskills' method
call = mohitSkils().myskills()  # Output: hello

# 'call' is the variable of 'mohitSkils'
# Without the 'self' method, we cannot access class methods
# Example of an error without 'self' method
# class helloSkils:
#     def myskills():
#         print("hello")
# call = helloSkils().myskills()  # This will raise an error

# To pass data within a class
# Example of passing data for one student
class newskills:
    def __init__(self, phonemunber, email_id):
        self.phone_number = phonemunber
        self.email_id = email_id

# Create an instance of 'newskills' with phone number and email ID
rohan = newskills(4739028739205, "qpmzj@example.com")
# Print the phone number and email ID of the instance 'rohan'
print(rohan.phone_number)  # Output: 4739028739205
print(rohan.email_id)      # Output: qpmzj@example.com



# Example of passing data for many students
class newskills:
    def __init__(self, phonemunber, email_id):
        self.phone_number = phonemunber
        self.email_id = email_id

    # Method to return student details
    def return_students(self):
        return self.phone_number, self.email_id

# Create an instance of 'newskills' with phone number and email ID
rohan = newskills(4739028739205, "qpmzj@example.com")
# Print the student details as a tuple
print(rohan.return_students())  # Output: (4739028739205, 'qpmzj@example.com')

# Variables inside a class are called class object variables
