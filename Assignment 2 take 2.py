


class Shirt:
    
    
    def __init__(self,shirt_quantity,shirt_type,shirt_color,shirt_cost):
            self.quantity = shirt_quantity
            self.type = shirt_type
            self.color = shirt_color
            self.cost = shirt_cost



    def Shirt_quant ():
        quantity = int(input("how many shirts would you like? "))
        print("you have selected %s shirts!"%(quantity))    

    def Shirt_type_find ():
        while True:
            shirttype= int(input("What type of shirt would you like? \n Type 1 for Polo or 2 for T-Shirt!"))
            if shirttype == (1):
                print("You have selected Polo shirts! ")
                break
            elif shirttype ==(2):
                print("You have selected T-Shirts!")
                break
            else:
                print ("Please input valid answer")

type_of_shirt = Shirt.Shirt_type_find()

number_of_shirts= Shirt.Shirt_quant()
print(type_of_shirt)
print(number_of_shirts)
    