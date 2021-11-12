class Student:

    school= "ACS/IT" #this is a class attribute

    def __init__(self, name, studentID):
        self.name = name #this is an instance atrribute
        self.studentID = studentID # also instance attribute

        #alice = Student ("Alice McBride", 12345)
        #bob = Student ("Bob Mckenzie", 23453)
        #carl = Student ("Carl Sagen", 982829)

    def description(self):
        return f"{self.name} has a student ID of: {self.studentID}"

    def grade(self,mark):
        return f"{self.name} has a mark of {mark}"

alice= Student ("Alice mcbride", 12345)    

print(alice.description,alice.name)