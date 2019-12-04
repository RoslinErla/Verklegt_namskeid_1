from model.employeeM import Employee
import string

class EmployeeLL():
    def __init__(self,inp):
        # self.__IOAPI = IOAPI()
        # self.__name = ""
        # self.__ssn= ""
        # self.__phone_number = "" 
        # self.__user_name = ""
        # self.__rank = ""
        self.__permit = ""
        self.__status = "At work"
        self.__inp = inp

    def validate_name(self):
        """Checks if name is valid and returns an error message if its not"""
        name = self.__inp.split()
        for elements in name:
            for letter in elements:
                if letter.isdigit() or letter in string.punctuation:
                    self.error_message(name)
        self.__name = self.__inp

    def validate_ssn(self):
        """Checks if the ssn is valid. Returns an error message if it is not"""
        if type(self.__inp) == int and len(str(self.__inp)) == 10:
            self.__ssn = self.__inp
        else:
            self.error_message(self.__inp)

    def validate_phone_number(self):
        """Checks if the phone number is valid. Returns an error message if it is not"""
        if type(self.__inp) == int and len(str(self.__inp)) == 7:
            self.__phone_number = self.__inp
        else:
            self.error_message(self.__inp)

    def validate_user_name(self):
        """Checks if the user name is valid. Returns an error message if it is not"""
        if len(self.__inp) >= 4:
            self.__user_name = self.__inp
        else: 
            self.error_message(self.__inp)
    
    def validate_rank(self):
        """Checks if the rank is valid, else it returns an error message"""
        if self.__inp.lower() == "flight attendant" or self.__inp.lower() == "flight service manager" \
            or self.__inp.lower() == "co-pilot" or self.__inp.lower() == "captain":
            self.__rank = self.__inp
        else:
            self.error_message(self.__inp)
    
    def validate_permit(self):
        if self.__inp != "":
            self.__permit = self.__inp #DONT KNOW WHAT TO VALIDATE HERE. DONT REALLY KNOW WhAT PERMITS YOU CAN HAVE
    
    def validate_status(self):
        if self.__status != self.__inp: 
            #valid check
            self.__status = self.__inp
            pass

    def add_employee(self):
        pass

    def change_employee(self):
        pass

    def error_message(self,Error):
        return "{} is invalid".format(Error)
