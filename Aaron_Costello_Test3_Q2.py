class Rectangle(object):
    def __init__(self):
        self.length=0
        self.width=0
    
    def getSize(self):
        self.length = int(input("What is the length?"))
        self.width = int(input("What is the width?"))


    def getPerimiter(self):
        self.perimiter = (self.length + self.width)*2
        
    def getArea(self):
        self.area = self.length*self.width

    def showResults(self):
        print("The area is:",self.area)
        print("The perimiter is:",self.perimiter)


obj1=Rectangle()
obj1.getSize()
obj1.getArea()
obj1.getPerimiter()
obj1.showResults()