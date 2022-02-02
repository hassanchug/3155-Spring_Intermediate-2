# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramaniam



class Student:

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    
    def report_gpa(self):
        return(self.name + " has a GPA of " + str(self.gpa))