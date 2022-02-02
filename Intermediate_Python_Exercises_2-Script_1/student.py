# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramaniam



class Student:
    
    # constructor that takes in a name and GPA and stores them both as instance fields
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    # creates report_gpa method that returns a string
    def report_gpa(self):
        return(self.name + " has a GPA of " + str(self.gpa))
