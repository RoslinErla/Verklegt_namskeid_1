from model.EmployeeM import Employee
import string

class Employee_LL():
    def __init__(self):
        # self.__IOAPI = IOAPI()
        self.__name = ""
        self.__ssn= ""
        self.__address = ""
        self.__phone_number = "" 
        self.__email = ""
        self.__rank = ""
        self.__permit = ""
        self.__status = ""

    def add_employee(self):
        pass

    def change_employee(self):
        pass

    def validate_name(self,name):
        """Checks if name is valid and returns an error message if its not"""
        name = name.split()
        for elements in name:
            for letter in elements:
                if letter.isdigit() or letter in string.punctuation:
                    return "{} is invalid".format(name)
        self.__name = name
    
    def validate_ssn(self,ssn):
        """Checks if the ssn is valid. Returns an error message if it is not"""
        if type(ssn) == int and len(str(ssn)) == 10:
            self.__ssn = ssn
        else:
            print("{} is invalid".format(ssn))
