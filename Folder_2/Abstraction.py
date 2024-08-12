# Demonstrating abstraction in Python using abstract base classes (ABC)

import abc

# Abstract base class 'MachineLearning' with three abstract methods
class MachineLearning():
    @abc.abstractmethod
    def Machine1(self):
        pass

    @abc.abstractmethod
    def Machine2(self):
        pass

    @abc.abstractmethod
    def Machine3(self):
        pass

# Printing the abstract method to show its type
print(abc.abstractmethod(MachineLearning))

# Concrete class 'DataScience' that inherits from 'MachineLearning' and implements all abstract methods
class DataScience(MachineLearning):

    def Machine1(self):
        return "this is machine 1"

    def Machine2(self):
        return "this is machine 2"

    def Machine3(self):
        return "this is machine 3"

# Creating an instance of 'DataScience' and calling the implemented method 'Machine1'
obj1 = DataScience()
print(obj1.Machine1())  # Output: this is machine 1
