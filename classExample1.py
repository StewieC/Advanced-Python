# creating a class and using the __init__() function
class Person:
    race = "black"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# the race is an instance that is shared by all instances of the class

# __init__ method initializes the name and age attributes when a new object is created

# creating an object of the Person class
stewie = Person("stewart", 21)
print("my name is ", stewie.name, " and I am ", stewie.age, " years old")
print("iam", stewie.race)