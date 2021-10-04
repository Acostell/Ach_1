userinput=input ("enter 1 to find prime, 2 to exit")
while userinput != 2:

    x = int (input("enter a whole number"))
    y = x -1
    isPrime = True

    while y != 1:
        
        if x%y == 0:
            isPrime = False
            break

        y = y -1

    if isPrime:
        print ("Is prime")

    else:
        print("Not prime")

    userinput=input ("enter 1 to find prime, 2 to exit")