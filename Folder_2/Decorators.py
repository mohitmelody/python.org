# The following code demonstrates the use of decorators to simplify repetitive tasks
# and enhance code readability. Decorators allow you to "wrap" functions with additional behavior.

import time

# Define a decorator named 'deco' which prints start and end messages around the execution of a function.
def deco(func):
    def inner_fun():
        print("start function")  # Print message before calling the decorated function
        func()  # Call the original function
        print("end method")  # Print message after the function execution
    return inner_fun()  # Return the result of calling inner_fun (note: this should be inner_fun, not inner_fun())

# Apply the 'deco' decorator to 'test1' function
@deco
def test1():
    # This is a placeholder for the main operations of the function
    print("this is my test function")

    # Example operation (commented out here)
    # print(796749 + 5608540)

# Calling the decorated 'test1' function will show the start and end messages
test1()


# Define another decorator 'deco' which measures and prints the execution time of a function.
def deco(func):
    def inside_fun():
        start = time.time()  # Record the start time
        func()  # Call the original function
        end = time.time()  # Record the end time
        total_time = end - start  # Calculate the time taken
        print(f"Execution time: {total_time} seconds")  # Print the execution time
    return inside_fun  # Return the wrapped function

# Apply the new 'deco' decorator to 'test1' function
@deco
def test1():
    # This is a placeholder for the main operations of the function
    print("this is my test function")

    # Example operation (commented out here)
    # print(796749 + 5608540)

# Calling the decorated 'test1' function will show the execution time
test1()
