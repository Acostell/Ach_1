#Assigntment 1, Make a store and show the commit and push after.
#Assignment 2, update and remaster assignment 1.

print("This assignment was to make a 'Storefront' for Abby's Merchandising (AM) including how many shirts, color, type and final price afterwards.")


print ("Welcome to Abby's Merchandizing!")


Shirt_cost = 9.99
while True:
    color = input("Please select a color of shirt!\n" "The color options are: Red, Blue, White and Black!")
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


print ("Now select a type of shirt! Type 1 for Polo or 2 for a T-Shirt!")

while True:
    ShirtType = input()

    if ShirtType == "1":
        print ("You have selected Polo shirts!")
        break
    elif ShirtType == "2":
        print ("You have selected T-Shirt!")
        break
    else :
        print(" Please select a valid shirt type '1' or '2'")    


Shirt_quantity = int(input("How many shirts would you like?\n" "They are $9.99 each!\n" "There is a 15'%' discount for purchases of 3 or more! "))

print ("You have selected %s shirts in total!"% (str(Shirt_quantity)))

shirt_total= Shirt_cost*Shirt_quantity
After_tax_cost = shirt_total * 1.13
after_discount10 = After_tax_cost *.9 
after_discount15 = After_tax_cost *.85
if Shirt_quantity >=3:
    quantity_discount = True
else:
    quantity_discount = False

print(" Are you a senior citizen or student?\n If yes to either please enter Y or yes, if no enter N or no ")
while True:
    senior_discount = str(input())
    if senior_discount == ("Y") or senior_discount == ("yes"):
        s_discount= True
        print("You qualify for a %10 discount! Your largest discount will be applied at checkout! ")
        break
    elif senior_discount == ("N") or senior_discount == ("no"):
        s_discount = False
        print("Sorry you don't qualify for the discount!")
        break
    else:
        print("Please put in a valid response.")

if quantity_discount == True:
    print ("Your cost before tax is $%.2f!" %(shirt_total))
    print ("Your cost after tax is $%.2f!" %(After_tax_cost)) 
    print("Your cost after discount is:$ %.2f" %(after_discount15))
    print ("This is with a 15% 'discount for quantity bought! ")

elif s_discount == True:
    print ("Your cost before tax is $%.2f!" %(Shirt_cost * Shirt_quantity))
    print ("Your cost after tax is $%.2f!" %(After_tax_cost))
    print("Your cost after discount is:$ %.2f" %(after_discount10))
    print ("This is with a %10 discount")

elif quantity_discount == True and s_discount == True:
    print ("Your cost before tax is $%.2f!" %(shirt_total))
    print ("Your cost after tax is $%.2f!" %(After_tax_cost))
    print("Your cost after discount is:$ %.2f" %(after_discount15))
    print ("Sorry only the largest discount is applied")

else:
    print ("Your cost before tax is $%.2f!" %(shirt_total))
    print ("Your cost after tax is $%.2f!" %(After_tax_cost))
    print("Your cost after discount is:$ %.2f" %(After_tax_cost))
    print ("No discounts were applied.")


print("Would you also like to purchase pants?")

while True:

    more = str(input("Yes or No?"))
    if more == "Yes":
        print("Great! Please continue to follow the prompts!")
        p = True
        break

    elif more == "No":
        print("Please proceed to payment, Have a great day!")
        print("You're total is:$%.2f" %(After_tax_cost))
        p = False
        break
    else:
        print(" Please enter Yes or No")


if p == True:
    
    while True:
        pant_color = str(input("Please select a color of Pants!\n" "The color options are: Navy, Blue or White Washed(WW)!"))
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
    

    pant_quantity = int(input("How many pants would you like? \n They are $12 each!"))
    print ("you have selected %s pants"%(pant_quantity))
    
    if pant_quantity >= 3:
        p_discount = True
   
    pant_total = pant_quantity * 12
    pant_total_afterTax= pant_total *1.13
    print ("Your Pants total before tax is :$%.2f" %(pant_total))

    if p_discount == True or s_discount == True:
        print ("Your total of shirts + pants is:$%.2f " %(float(Shirt_quantity*Shirt_cost)+(pant_total)))
        print ("Your total of shirts + pants after tax is :$%.2f "%((shirt_total+pant_total)*1.13))    
        print ("Your total after tax and discounts is :$%.2f" %(float(After_tax_cost+pant_total_afterTax)*.85))

    elif p_discount == False and s_discount == True:
        print ("Your total of shirts + pants is:$%.2f " %float(Shirt_quantity*Shirt_cost)+(pant_total))
        print ("Your total of shirts + pants after tax is :$%.2f "%(float(shirt_total+pant_total)*1.13))   
        print ("Your total after tax and discounts is :$%.2f" %(float(After_tax_cost+pant_total_afterTax)*.9))
    else:
        print ("Your total of shirts + pants is:$%.2f " %float((Shirt_quantity*Shirt_cost)+(pant_total)))
        print ("Your total of shirts + pants after tax is :$%.2f "%(float(shirt_total+pant_total)*1.13))   
        print ("Your total after tax and discounts is :$%.2f" %(float(After_tax_cost+pant_total_afterTax)))
    
    print ("Please proceed to payment")

else: 
    pass
