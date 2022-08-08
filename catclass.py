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
    def __init__(self, name):
        super().__init__(name)

class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def meow(self):
        e=MyException("Nope, scratch scratch")
        try:
            if super().meow():
                raise MyException("Invalid")
        except MyException as e:
            print(e.message)
        finally:
            print("Program Stop")




cat_1=Cat('Oreo')
print(cat_1.name)
cat_1.meow()