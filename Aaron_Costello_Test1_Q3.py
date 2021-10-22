


class Temperatures:
    def __init__(self,name):
        self.name = name
        self.temp = []

    def enterTemp(self):
        for i in range (3):
            a = float(input("Enter temperature of %s on day %d " %(self.name,i+1)))
            self.temp.append(a)

    def displayTemp(self):
        print(self.name, "had a temperature of ", self.temp)
        

    def calcAverageTemp (self):
        summation = sum(self.temp)
        average = summation/len(self.temp)
        print ("The average temp of %s over the days was:" %str(self.name),str(average))

location1= Temperatures("Brampton")
location1.enterTemp()

location2= Temperatures("Windsor")
location2.enterTemp()

location3= Temperatures("Oakville")
location3.enterTemp()


location1.displayTemp()
location2.displayTemp()
location3.displayTemp()

location1.calcAverageTemp()
location2.calcAverageTemp()
location3.calcAverageTemp()