class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
student1 = Student("stewie", 21)
print(student1)

# __str__ implementation: uses the self parameter to access the instance's attributes

"""
when print(student1) is called, python automatically uses the __str__ method
to get a string representation of the object.
Without __str__, calling print(student1) would produce something like <__main__.Student object at 0x00000123>.

"""