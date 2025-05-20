# creating a parent class
class Animal:
    def __init__(self, name):
        self.name = name
        
        
    def speak(self):
        pass
    
# creatinga child class that will inherit from parent class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
dog = Dog("jimy")
print(dog.speak())  # Output: jimy says Woof!