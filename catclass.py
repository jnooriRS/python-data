class Cat:
    def __init__(self, name):
        self.name = name
    
    def meow(self):
        print("meow")

class GoodCat(Cat):
    def __init__(self, name):
         super().__init__(name)

    def meow(self):     
        print("purr purr meow")
    
class BadCat(Cat):
    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        print("hiss")
        return True
    
class VeryBadCat(Cat):
    def meow(self):
        raise MyException("Nope, scratch scratch") 

class MyException(Exception):
    def __init__(self, message):
        self.message = message
        
cat_1=Cat('Oreo')
print(cat_1.name)
cat_1.meow()