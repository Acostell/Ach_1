from time import localtime, strftime

now= strftime("%B, %A %Y, %H:%M:%S",localtime())
print(now)