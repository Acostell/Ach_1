from time import localtime, strftime

now= strftime("%A, %B %Y, %H:%M:%S",localtime())
print(now)