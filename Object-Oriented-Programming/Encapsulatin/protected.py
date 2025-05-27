# protected members are identified with a single underscore

# they are meant to be accessed only within the class or its subclasses

class Protected:
    def __init__(self):
        self._age = 21
        
class Subclass(Protected):
    def disp(self):
        print(self._age)
        
obj = Subclass()
obj.disp()