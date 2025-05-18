class Person():
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
    # create a static method to check if a person is an adult or not
    @staticmethod
    def isAdult(age):
        return age > 18
    
if __name__ == "__main__":
    res = Person.isAdult(10)
    print("is person adult? ",res)
    
    res = Person.isAdult(21)
    print("\nis person adult? ",res)
    
    
