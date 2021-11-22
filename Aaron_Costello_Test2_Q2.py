class LargestValue(object):
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def maxvalue(num1,num2,num3):
        list1 = [num1,num2,num3]
        print("the largest number is:", (float(max(list1))))

num1 = float(input("input first number: "))
num2 = float(input("input second number: "))
num3 = float(input("input third number: "))

LargestValue.maxvalue(num1,num2,num3)