class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

    def display(self):
        print(f"{self.name}, id:{self.id}")
        
koshy = Student("koshy", 2250)
koshy.display()
