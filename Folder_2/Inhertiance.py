# Demonstrating inheritance in Python

# Base class 'test' with a method 'test_matg' also callled parent class
class test:
    def test_matg(self):
        return 'this is my class test'

# 'child_test' inherits from 'test' but does not add any new functionality
class child_test(test):
    pass

# Creating an instance of 'child_test' and calling the inherited method 'test_matg'
child_test1 = child_test()
print(child_test1.test_matg())  # Output: this is my class test

# Base class 'article' with methods 'data', '__init__', and 'return_data'
class article:
    def data(self):
        return 'this is my class article'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def return_data(self):
        return self.name, self.age

# 'article1' inherits from 'article' and adds a new method 'dat2'
class article1(article):
    def dat2(self):
        return 'this is my class article1'

# 'article2' inherits from 'article' but does not add any new functionality
class article2(article):
    pass

# Creating an instance of 'article2' and calling the inherited method 'return_data'
obj_class = article2(name="mohit", age=21)
print(obj_class.return_data())  # Output: ('mohit', 21)
