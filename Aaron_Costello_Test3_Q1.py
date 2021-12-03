from time import localtime, strftime

now= strftime("%A, %B %d, %H:%M:%S",localtime())
print(now)