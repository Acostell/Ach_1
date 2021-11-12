class LargestValue(object):
    def __init__(self,num1,num2,num3):
        num1= num1
        num2= num2
        num3= num3

    def maxvalue(num1,num2,num3):
        list1=[num1,num2,num3]
        print("the largest number is:", (int(max(list1))))

num1 =int(input("input first number"))
num2 = int(input("input second number"))
num3 = int(input(" input third number"))

LargestValue.maxvalue(num1,num2,num3)