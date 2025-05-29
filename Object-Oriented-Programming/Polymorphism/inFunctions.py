# duck typing enables functions to work with any object regardless of the type

def add(a, b):
    return a + b

print(add(10, 11))
print(add("stewart", " comfort"))

# polymorphism in operators

print(5 + 10)