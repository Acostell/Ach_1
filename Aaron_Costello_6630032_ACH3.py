x = int (input("Input a whole number:"))
sum = 0

while x > 0:
    if x % 2 ==0:
        sum += x**2
        x = x-1
    else:
        x=x-1
    if x == 0:
        print(sum)
 