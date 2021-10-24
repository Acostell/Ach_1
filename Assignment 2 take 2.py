
class Shirt:
    
    
    def __init__(self):
            self.quantity = 
            self.type = 
            self.color = 
            self.cost = 



    def Shirt_quant (self):
        self.quantity = int(input("How many shirts would you like?"))
            
    def shirt_quant_repeat(self):
        print("you have selected: %s shirts!" %(self.quantity))


    def Shirt_type_find (self):
        while True:
            shirt_type= int(input("What type of shirt would you like? \n Type 1 for Polo or 2 for T-Shirt!"))
            if shirt_type == (1):
                print("You have selected Polo shirts! ")
                break
            elif shirt_type ==(2):
                print("You have selected T-Shirts!")
                break
            else:
                print ("Please input valid answer")

shirt_buy= Shirt()

