import os
path= "C:\Conestoga\PROG1783\Ach_1\\"
file2name="File3.txt"
file1= open("PROG1783File1Before.txt")

file2= open("File3.txt",'w')

file2.write(file1.read(100))
file1.close()
file2.close()
os.rename(file2name,path + 'PROG1783File1After.txt')

