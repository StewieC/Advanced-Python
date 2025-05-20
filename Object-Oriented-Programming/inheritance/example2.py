class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        
    def disp(self):
        print(f"Name: {self.name}, Course: {self.course}")
        
        
class Koshy(Student):
    
    def print(self):
        print("student details:\n ------------------------")
        
res = Koshy("Koshy", 2250)
res.print()
res.disp()