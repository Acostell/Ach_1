#Assigntment 1, Make a store and show the commit and push after.
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


After_tax_cost = Shirt_cost * 1.13

print ("Your cost before tax is $%.2f!" %(Shirt_cost))

print ("Your cost after tax is $%.2f!" %(After_tax_cost)) 

print ("Please procceed to payment and have a nice day!")

