# python uses reference counting to manage memory

# each object keeps track of howmany references point to it
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  
# here x is referenced twice, once by x and once by getrefcount


y = x   
print(sys.getrefcount(x))  
# assgning y = x increases the count

y = None
print(sys.getrefcount(x))  
# when the reference count reaches 0, the object is deallocated