class Student(object):

    def __init__(self,studentName, studentId, studentGrades):
       info = studentName + ' '+ studentId + ' ' + studentGrades
       print(" The students information is : " + str(info))

collection = Student()
collection.__init__(input("Name "),input("ID# "),input("Grades "))
