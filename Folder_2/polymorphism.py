# Polymorphism - ek object se multiple form se represent kar sakte hai, multiple kaam karta hai

# In object-oriented programming, polymorphism is used to create
# objects that can be used in different contexts without having to create separate objects
# for each context. This allows for more flexibility and reusability in programming.

# Define a class named 'datScience'
class datScience:
    # Define a method 'syllabus' that prints a message
    def syllabus(self):
        print("this is data science class")

# Define another class named 'datScience1'


class datScience1:
    # Define a method 'syllabus' that prints a message
    def syllabus(self):
        print("this is data science class 1")

# Define another class named 'datScience2'


class datScience2:
    # Define a method 'syllabus' that prints a message
    def syllabus(self):
        print("this is data science class 2")

# Define a function 'syllable' that takes a list of class instances


def syllable(class_ki_instance):
    # Iterate over each instance in the list
    for i in class_ki_instance:
        # Call the 'syllabus' method of each instance
        print(i.syllabus())


# Create an instance of 'datScience'
data1 = datScience()
# Call the 'syllabus' method of 'data1' and print the result
print(data1.syllabus())  # Output: this is data science class

# Create an instance of 'datScience1'
data2 = datScience1()
# Call the 'syllabus' method of 'data2' and print the result
print(data2.syllabus())  # Output: this is data science class

# Create an instance of 'datScience2'
data3 = datScience2()
# Call the 'syllabus' method of 'data3' and print the result
print(data3.syllabus())  # Output: this is data science class

# Create a list of class instances
class_ki_instance = [data1, data2, data3]
# Call the 'syllable' function with the list of class instances
syllable(class_ki_instance)
