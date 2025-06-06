from abc import ABC, abstractmethod
class Dod(ABC):
    def  __init__(self, name):
        self.name = name
        
    @abstractmethod
    def sound(self):
        pass
    
    def display(self):
        print(f"{self.name} makes a sound: {self.sound()}")
        
class Labrador(Dog):  # Partial Abstraction
    def sound(self):
        print("Labrador Woof!")

class Beagle(Dog):  # Partial Abstraction
    def sound(self):
        print("Beagle Bark!")

# Example Usage
dogs = [Labrador("Buddy"), Beagle("Charlie")]
for dog in dogs:
    dog.display_name()  # Calls concrete method
    dog.sound()  # Calls implemented abstract method