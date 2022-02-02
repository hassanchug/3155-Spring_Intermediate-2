# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramaniam

# import the Student class
from student import Student
# instantiate with a name and gpa
studentRep = Student("Oliver", 2.45)
# stores both as an instance by calling the report_gpa method
report = studentRep.report_gpa()
# prints the instance calling the method
print(report)
