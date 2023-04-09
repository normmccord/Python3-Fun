# create a class that passes inheritance to child classes

# the parent class
import datetime

class Person:
    def __init__(self, fn, mn, ln):
        self.fname = fn
        self.mname = mn
        self.lname = ln
        self.gender = 2
        self.ID = "0000000000"
        self.bday = datetime.datetime(1000, 1, 1)

    # gender
    def get_gender(self):
        if self.gender == 0:
            return "M"
        elif self.gender == 1:
            return "F"
        else:
            return "O"

    def set_gender(self, new_gender):
        if new_gender >= 0 and new_gender <= 2:
            self.gender = new_gender
            return True
        else:
            return False

    # birthday (import datetime)
    def set_birthday(self, month, day, year):
        if month > 12 or month < 1:
            return False
        if day > 31 or day < 1:
            return False
        if year < 1:
            return False
        self.bday = datetime.datetime(year, month, day)

    def get_birthday(self):
        return self.bday

    def get_age(self, month, day, year):
        c = datetime.datetime(year, month, day)
        return (c - self.bday)/365.25



