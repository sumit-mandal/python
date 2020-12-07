
# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())

# base class ke  andar  parent class k method ko implement krwaana hi padega, kaise b krke
#shape class se agr inherit kr rhe hai to zaroori hai implement krwaana use function ko base class k andar
