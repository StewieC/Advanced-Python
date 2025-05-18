class Math():
    
    @staticmethod
    def add(x, y):
        return x + y
    
if __name__ == "__main__":
    # call the method of the class without creating instance
    res = Math.add(3, 4)
    print("result ", res)