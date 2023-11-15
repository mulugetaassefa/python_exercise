class Mamal:
    def walk(self):
        print("walk")
class Dog(Mamal):
    def bark(self):
        print("bark")

class Cat(Mamal):
    pass
dog1=Dog()
cat1=Cat()
dog1.walk()
dog1.bark()
cat1.walk()