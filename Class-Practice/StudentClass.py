


import datetime
from Classes import Person


# the child class
class Student(Person):
    def __init__(self, fn, mn, ln):
        Person.__init__(self, fn, mn, ln)
        self.gpa = 0.0
        self.credits = 0.0
        self.major = "NONE"
        self.registration_time = "0-0-0000"
        self.fin_aid = 0.0
        self.on_campus = False

# setters and getters
    # GPA
    def set_gpa(self, new_gpa):
        if new_gpa >= 0 and new_gpa <= 4.0:
            self.gpa = new_gpa
            return True
        else:
            return False
    def get_gpa(self):
        return self.gpa

    # credits
    def set_credits(self, new_creds):
        if new_creds >= 0:
            if new_creds >= self.credits:
                self.credits = new_creds
                return True
            else:
                return False
        else:
            return False
    def get_creds(self):
        return self.credits