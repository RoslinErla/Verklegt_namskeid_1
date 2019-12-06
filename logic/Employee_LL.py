from model.employeeM import Employee
import string

class EmployeeLL():
    def __init__(self,inp):
        #TENGSL VIÐ IO
        self.__name = ""
        self.__ssn= ""
        self.__phone_number = "" 
        self.__user_name = ""
        self.__rank = ""
        self.__permit = ""
        self.__status = "At work"
        self.__inp = inp

    def validate_name(self):
        """Checks if name is valid and Returns True if it is valid"""
        name = self.__inp.split()
        for elements in name:
            for letter in elements:
                if letter.isdigit() or letter in string.punctuation:
                    return False
        self.__name = self.__inp
        return True

    def validate_ssn(self):
        """Checks if the ssn is valid. Returns True if it is valid"""
        if type(self.__inp) == int and len(str(self.__inp)) == 10:
            self.__ssn = self.__inp
            return True

    def validate_phone_number(self):
        """Checks if the phone number is valid. Returns True if it is valid"""
        if type(self.__inp) == int and len(str(self.__inp)) == 7:
            self.__phone_number = self.__inp
            return True

    def validate_user_name(self):
        """Checks if the user name is valid. Returns True if it is valid"""
        if len(self.__inp) >= 4:
            self.__user_name = self.__inp
            return True
    
    def validate_rank(self):
        """Checks if the rank is valid. Returns True if it is valid"""
        if self.__inp.lower() == "flight attendant" or self.__inp.lower() == "flight service manager" \
            or self.__inp.lower() == "co-pilot" or self.__inp.lower() == "captain":
            self.__rank = self.__inp
            return True

    def validate_status(self):
        if self.__status != self.__inp: 
            if self.__inp == ("not at work" or "on vacation"): 
                self.__status = self.__inp
                return True

    def add_employee(self):
        pass

    def change_employee(self):
        pass
