# use a driver file to build an object from a class
import datetime

# you can import one class from a file full of classes, or the entire file
from StudentClass import Student
from Classes import Person

# create some objects from the imported class
# input arguments in the way they are set up in the class file
s1 = Student("Bob", "J", "Simpson")
# s2 = Student("Jim", "H", "Sampson")

# use the Class functions to give the objects new attributes
x = float(input("Enter GPA: "))
while not s1.set_gpa(x):
    x = float(input("Enter GPA: "))


s1.set_birthday(3, 18, 2023)

print(s1.fname, s1.get_gpa(), s1.get_age(3, 19, 2023))
# print(s2.fname, s2.get_gpa())
