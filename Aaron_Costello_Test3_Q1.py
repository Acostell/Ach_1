from time import localtime, strftime

now= strftime("%m:%d:%Y , %H:%M:%S",localtime())
print(now)