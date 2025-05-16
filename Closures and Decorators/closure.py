# create an outer function that takes x
def fun1(x):
    
    # create an inner function that takes y
    def fun2(y):
        
        #capture x from the outer function
        return x + y
    
    # return the inner function as the closure
    return fun2

# create a closure by calling the outter function
clos = fun1(10)

# now we can use the closure, which remembers the value x as 10
print(clos(2))