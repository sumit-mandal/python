class Animal():
    def __init__(self):
        print("Animal Created")

    def WhoAmI(self):
        print("Animal")

    def eat(self):
        print("eating")


class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("Woof")


    def eat(self):
        print("Dog eating")


myd=Dog()
myd.WhoAmI()
myd.eat()
myd.bark()
myd.eat()
