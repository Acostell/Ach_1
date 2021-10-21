class Studentgrades:
    def __init__(self,name, science,math,chemistry,physed,itsupport):
        self.name = name
        self.science = science
        self.math = math
        self.chemistry = chemistry
        self.physed = physed
        self.itsupport = itsupport

    def grades (self):
        [science,math,chemistry,physed,itsupport]=input()

aaron = Studentgrades ("Aaron",science,math,chemistry,physed,itsupport)
        