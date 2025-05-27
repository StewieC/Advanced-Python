# public members

class Public:
    def __init__(self):
        self.name = "stewie" # a public attribute
        
    def disp(self):
        print(self.name) # public method
        
obj = Public()
obj.disp()  # accessible
print(obj.name)  # accessible