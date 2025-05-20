class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Baby(Person):
    def __init__(self, name, age, id, school):
        super().__init__(name, age)
        self.id = id
        self.school = school
        
    def display(self):
        print(f"{self.name}, id:{self.id} is {self.age} years old learning in {self.school}")
        
        
baby = Baby("jermaine", 21, 2250, "engineering School")
baby.display()