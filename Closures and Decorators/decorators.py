# a simple decorator function

def decorator(func):
    def wrapper():
        print("before calling the function \n")
        
        func()
        print("after calling the function")
        
    return wrapper
# applying the decorator to a function
@decorator
def greet():
    print("hey!")
    
# calling the decorated function
greet()

"""
EXPLANATION:

decorator takes the greet function as an argument

it returns a new function (wrapper) that first prints a message, calls greet() then prints another message

"""