class Rectangle(object):
    def __init__(self):
        self.length = int(input)
        self.width = int(input)
        



    def calcArea(self):
        self.length()
        self.width()
        area = self.length * self.width
        return (area)

shape1 = Rectangle()
shape1.calcArea()