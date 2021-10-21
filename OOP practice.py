class Car:
    company= "Ford"
    
    def __init__ (self,model,color,mileage,year):
        
        self.model = model
        self.color = color
        self.mileage = mileage
        self.year = year

        #fiesta= Car ("Fiesta","Red",125000,2020)
        #focus= Car ( "Focus", "Green", 68000,2019)
        #escort= Car ( "Escort", "Black", 500, 2022)

    def description (self):
        return f"{self.model} has a color of {self.color}."

    def distance (self):    
        return f"{self.model} has a mileage of {self.mileage}."

    def runyear (self):
        return f"{self.model} Has the year make of {self.year}."    

        
fiesta= Car ("Fiesta","Red",125000,2020)
focus= Car ( "Focus", "Green", 68000,2019)
escort= Car ( "Escort", "Black", 500, 2022)

print((input().description()),fiesta.distance(),fiesta.runyear())