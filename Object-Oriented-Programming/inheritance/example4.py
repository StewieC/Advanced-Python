class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def display(self):
        print(self.name)
        print(self.id)
        
class Student(Person):
    def __init__(self, name, id ,school):
        super().__init__(name, id)
        self.school = school
        
    def student_display(self):
        print(f"{self.name}, id:{self.id} is learning in {self.school}")
        
koshy = Student("koshy", 2250, "engineering School")
koshy.display()
koshy.student_display()