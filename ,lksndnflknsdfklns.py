cost = 10.5
while True:
    x=input("are you a senior or a student (yes/y) or (no/n)")    
    if x == "yes" or x == "y":
        print("You qualify for a discount!")
        cost *= .9
        break
    elif x == "n" or x == "No":
        print("Sorry, you dont qualify for a discount!")
        break
    else:
        print("Please input a valid response")
print ("price after discount is:%.2f!" %(cost))