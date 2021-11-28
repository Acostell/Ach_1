


class Shirts(object):
    
    def __init__(self):
        self.shirtPrice = 9.99
        self.shirtQuantity = 0
        
    def sQuantityPrompt(self):

        sQ = int(input("How many shirts would you like to buy?\n They are $9.99 each, with a 15% discount for 3 or more!\n "))
        self.shirtQuantity += sQ
            

    def sColorPrompt(self):
        while True:
            color = input("Please select a color of shirt!\n" "The color options are: Red, Blue, White and Black!\n ")
            self.scolor = color
            if color == "Red":
                print("You have chosen a red shirt!")
                break
            elif color == "Blue":
                print ("you have chosen Blue!")     
                break
            elif color == "White":
                print ("you have chosen White!")
                break
            elif color == "Black":
                print ("You have chosen Black")
                break
            else :
                print ("Please select a valid color from the options!")

    def shirtType(self):
        while True:
            ShirtType = input("Now select a type of shirt! Type 1 for Polo or 2 for a T-Shirt!\n ")

            if ShirtType == "1":
                print ("You have selected Polo shirts!")
                self.sType = "Polo Shirts"
                break
            elif ShirtType == "2":
                print ("You have selected T-Shirt!")
                self.sType = "T-Shirts"
                break
            else :
                print(" Please select a valid shirt type '1' or '2'")
            
            
class Pants(object):
    def __init__(self):
        self.pantPrice = 12.00
        self.pantQuantity = 0


    def pQuantityPrompt(self):

            pQ = int(input("How many Pants would you like to buy?\n They are $12.00 each!\n "))
            self.pantQuantity += pQ
                

    def pColorPrompt(self):
        while True:
            color2 = input("Please select a color of shirt!\n" "The color options are: Red, Blue, White and Black!\n ")
            self.pcolor = color2
            if color2 == "Red":
                print("You have chosen a red shirt!")
                break
            elif color2 == "Blue":
                print ("you have chosen Blue!")     
                break
            elif color2 == "White":
                print ("you have chosen White!")
                break
            elif color2 == "Black":
                print ("You have chosen Black")
                break
            else :
                print ("Please select a valid color from the options!")

    def pantType(self):
        while True:
            pantType = input("Now select a type of shirt! Type 1 for Polo or 2 for a T-Shirt!\n ")

            if pantType == "1":
                print ("You have selected Polo shirts!")
                self.pType = "Polo Shirts"
                break
            elif pantType == "2":
                print ("You have selected T-Shirt!")
                self.pType = "T-Shirts"
                break
            else :
                print(" Please select a valid shirt type '1' or '2'")


class Calculate(object):

    def __init__(self):
        self.total= 0.00
    
    def calcDiscount(self,quantity):

        if  quantity >= 3:
            self.q_discount = True
        else:
            self.q_discount = False


        while True:
            senior_discount = str(input(" Are you a senior citizen or student?\n If yes to either please enter Y or yes, if no enter N or no "))
            if senior_discount == ("Y") or senior_discount == ("yes"):
                self.s_discount= True
                print("You qualify for a %10 discount! Your largest discount will be applied at checkout! ")
                break
            elif senior_discount == ("N") or senior_discount == ("no"):
                self.s_discount = False
                print("Sorry you don't qualify for the discount!")
                break
            else:
                print("Please put in a valid response.")


    def calcTotal(self,quantity,price):
        self.total += quantity * price
        if self.q_discount == True:

            print ('Your total is:$',self.total)


print ("Welcome to Abby's Merchandising!\n What would you like to buy?")

   

sale1 = Shirts()

sale1.sQuantityPrompt()
sale1.sColorPrompt()
sale1.shirtType()

sale1total = Calculate()
sale1total.calcDiscount(sale1.shirtQuantity)
sale1total.calcTotal(sale1.shirtQuantity,sale1.shirtPrice)

print('The shirts you have selected are:', sale1.shirtQuantity, sale1.scolor, sale1.sType)




