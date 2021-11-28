


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
            pant_color = str(input("Please select a color of Pants!\n" "The color options are: Navy, Blue or White Washed(WW)!"))
            self.pcolor = pant_color
            if pant_color == "Navy":
                print("You have chosen Navy!")
                break

            elif pant_color == "Blue":
                print ("you have chosen Blue!")     
                break

            elif pant_color == "White" or pant_color == "WW":
                print ("you have chosen White Washed!")
                break

            else :
                print ("Please select a valid color from the options!")

    def pantType(self):
        while True:
            pant_type = str(input("Please select a type of pants now: \n The options are Tight or Loose."))

            if pant_type == "Tight":
                print ("You have selected Tight pants!")
                break

            elif pant_type == "Loose":
                print ("You have selected Loose pants")        
                break
            
            else:
                print ("Please select a valid option")


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
        self.total += (quantity * price)
        self.total_aftertax = self.total*1.13
        
        

        if self.q_discount == True:

            self.total_after_discount = self.total_aftertax * .85

        elif self.q_discount == False and self.s_discount == True:

            self.total_after_discount = self.total_aftertax * .90

        else:
            self.total_after_discount = self.total_aftertax

        

            
            

        

print ("Welcome to Abby's Merchandising!")

   
p=False
sale1 = Shirts()

sale1.sQuantityPrompt()
sale1.sColorPrompt()
sale1.shirtType()

sale1total = Calculate()
sale1total.calcDiscount(sale1.shirtQuantity)
sale1total.calcTotal(sale1.shirtQuantity,sale1.shirtPrice)
print("Your total after tax and discounts is:$%.2f"%(sale1total.total_after_discount))

print('The shirts you have selected are:', sale1.shirtQuantity, sale1.scolor, sale1.sType)




while True:
    print("Would you like to also buy pants?")
    more = str(input("Yes or No?"))
    if more == "Yes":
        print("Great! Please continue to follow the prompts!")
        p = True
        break

    elif more == "No":
        print("Please proceed to payment, Have a great day!")
        sale1total.calcTotal(sale1.shirtQuantity,sale1.shirtPrice)
        p = False
        break
    else:
        print(" Please enter Yes or No")

if p == True:
    
    sale2=Pants()
    sale2.pQuantityPrompt()
    sale2.pColorPrompt()
    sale2.pantType()

    sale2total=Calculate()
    sale2total.calcDiscount(sale2.pantQuantity)
    sale2total.calcTotal(sale2.pantQuantity,sale2.pantPrice)
    
    if sale1total.q_discount == True and sale2total.q_discount == True:

        sale2total.total_after_discount = (sale1total.total_aftertax + sale2total.total_aftertax) *.85
        print("Your total after tax and discounts for both shirts and pants are:$%.2f"% (sale2total.total_after_discount))
    else:   
        print("Your total after tax and discounts for both shirts and pants are:$%.2f"% (sale2total.total_after_discount + sale1total.total_after_discount))
else:
    pass    