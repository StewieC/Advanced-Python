class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

    def display(self):
        print(f"{self.name}, id:{self.id}")
        
class Son:
    def __init__(self, age):
        self.age = age
        
class StudentSonPerson(Student, Son):
    def __init__(self, name, id, age):
        Student.__init__(self, name, id)
        Son.__init__(self, age)
        
    def display(self):
        print(f"{self.name}, id:{self.id}, age:{self.age}")
        
koshy = StudentSonPerson("koshy", 2250, 21)
koshy.display()