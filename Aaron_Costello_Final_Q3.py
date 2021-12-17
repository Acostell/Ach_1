import datetime


class AnalyzeTriangle:
    def __init__(self):
        self.side1=side1
        self.side2=side2
        self.side3=side3
     


    def validateTriangle(self):
        
        if self.side1 + self.side2 + self.side3 == 180:
            if self.side1 == self.side2 and self.side1 == self.side3:
                print("This is an Equalateral Triangle")
                
            if self.side1 == self.side2 and self.side1 != self.side3:
                print("This is an Isosceles Triangle")

            if self.side1 != self.side2 and self.side1 == self.side3:
                print("This is an Isosceles Triangle") 

            if self.side3 != self.side1 and self.side2 == self.side3:
                print("This is an Isosceles Triangle") 
            elif self.side1 != self.side2 and self.side1 != self.side3:
                print("This is a Scalene Triangle")
                
        else:
            print("This is not a triangle!")    



        
            
date= datetime.datetime.now()
triangle=False
side1= int(input("Side 1 Angle:"))
side2= int(input("Side 2 Angle:"))
side3= int(input("Side 3 Angle:"))

triangle1=AnalyzeTriangle()
triangle1.validateTriangle()
print(date.strftime("%m/%d/%Y %H:%M:%S"))