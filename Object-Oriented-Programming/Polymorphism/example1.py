"""
in oop polymorphism allows methods in different classes toshare same name but perform distinct tasks

this is achieved through inheritance and nterface design


"""
class Shape:
    def area(self):
        return "undefined"
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width