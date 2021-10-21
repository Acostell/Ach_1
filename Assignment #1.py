#Assigntment 1, Make a store and show the commit and push after.
"y" or "Y" or "yes" or "Yes" = True 

print("This assignment was to make a 'Storefront' for Abby's Merchandising (AM) including how many shirts, color, type and final price afterwards.")



print ("Welcome to Abby's Merchandizing!")

print ("Please select a color of shirt you would like!")

print (" the color options are: Red, Blue, White and Black!")

color = input()

if color == "Red":
    print("You have chosen a red shirt!")

elif color == "Blue":
    print ("you have chosen Blue!")     

elif color == "White":
    print ("you have chosen White!")

elif color == "Black":
    print ("You have chosen Black")

else :
    print ("Please select a valid color from the options!")


print ("Now select a type of shirt! Type 1 for Polo or 2 for a T-Shirt!")

ShirtType = input()

if ShirtType == "1":
    print ("You have selected Polo shirts!")

elif ShirtType == "2":
    print ("You have selected T-Shirt!")

else :
    print(" Please select a valid shirt type '1' or '2'")    

quantity = int(input("How many shirts would you like?"))

print ("You have selected %s shirts in total!"% (str(quantity)))

cost = quantity * 9.99

aftertaxcost = cost * 1.13

print ("Your cost before tax is $%.2f!" %(cost))

print ("Your cost after tax is $%.2f!" %(aftertaxcost)) 

print ("Please procceed to payment and have a nice day!")

