import re
import datetime
date= datetime.datetime.now()
def replace(name,fixed):
    with open("C:\Conestoga\PROG1783\Ach_1\PROG1783 Final Exam\PROG1783File2.txt","r+") as f:
        file= f.read()
        file= re.sub(name,fixed,file)
        f.write(file)
        f.close
name = "Aaron"
fixed = "********" 
print(replace(name,fixed))

file1=open("C:\Conestoga\PROG1783\Ach_1\PROG1783 Final Exam\PROG1783File2.txt",'a')
file1.write(date.strftime("%m/%d/%Y %H:%M:%S"))
file1.close
file1= open("C:\Conestoga\PROG1783\Ach_1\PROG1783 Final Exam\PROG1783File2.txt",'r')
print(file1.read())
#not sure how to incorperate \n to make it seperate maybe import terminal and newline?