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
        
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius
    
shapes = [Rectangle(2,3), Circle(10)]
for shape in shapes:
    print(f"Area: {shape.area()}")  # polymorphism in action, same method name, different implementations