
def factorial(x):
     if x == 0:
         return 1
     else:
         return x * factorial(x-1)
        

x=int(input("input a number to be factorialed "))
print(factorial(x))