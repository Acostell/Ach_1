class Calculator(object):

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def addition(num1,num2):
        print (num1+num2)

    def subtraction (num1,num2):
        print (num1 - num2)

    def multiplication (num1,num2):
        print (num1 * num2)

    def division (num1,num2):
        print(num1/num2)

    def modulusDiv (num1,num2):
        print(num1 % num2)

num1 = float(input("input the first number: "))
num2 = float(input("input the second number: "))



while True:
    choice = int(input("what would you like to do with these numbers: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for modulus division!"))
    if choice == 1:
        Calculator.addition(num1,num2)
        break

    elif choice == 2:
        Calculator.subtraction(num1,num2)
        break

    elif choice == 3:
        Calculator.multiplication(num1,num2)
        break

    elif choice == 4:
        Calculator.division(num1,num2)
        break

    elif choice == 5:
        Calculator.modulusDiv(num1,num2)
        break

    else:
        print("Select from 1 to 5")                   

