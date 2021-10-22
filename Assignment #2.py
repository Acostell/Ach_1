#Assigntment 1, Make a store and show the commit and push after.
print("This assignment was to make a 'Storefront' for Abby's Merchandising (AM) including how many shirts, color, type and final price afterwards.")

print ("Welcome to Abby's Merchandizing!")

print("Would you like to purchase a shirt?")

Shirt = input("yes or no")

while True:
    if Shirt == "yes":
        Shirt= True
        break
    elif Shirt =="no":
        Shirt= False
        break
    else:
        print("try again")    

Shirt_cost = 9.99

while Shirt == True:
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

while Shirt == True:
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

while Shirt == True:
    x=input("are you a senior or a student (yes/y) or (no/n)")    
    if x == "yes" or x == "y":
        print("You qualify for a discount!")
        Shirt_cost *= .9
        break
    elif x == "n" or x == "No":
        print("Sorry, you dont qualify for a discount!")
        break
    else:
        print("Please input a valid response")
print ("price after discount is:%.2f!" %(Shirt_cost))

After_tax_cost = Shirt_cost * 1.13

print ("Your cost before tax is $%.2f!" %(Shirt_cost))

print ("Your cost after tax is $%.2f!" %(After_tax_cost)) 

print ("Please procceed to payment and have a nice day!")

