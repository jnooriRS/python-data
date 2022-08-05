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
    
class VeryBadCat(Cat):
    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        try:
            if super().meow():
                return True
            raise Exception
        except Exception('My exception') as e:
            print(e)
        finally:
            print("Stop")




cat_1=Cat('Oreo')
print(cat_1.name)
cat_1.meow()