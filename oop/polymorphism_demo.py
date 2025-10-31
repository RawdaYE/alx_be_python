import math

class Shape:
    def area():
        raise NotImplementedError("haven't implemented yet!")
    


class Rectangle(Shape):
    def __init__(self, height, length):
        super().__init__()
        self.height = height
        self.length = length

    def area(self):
        return self.height * self.length


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius **2 
