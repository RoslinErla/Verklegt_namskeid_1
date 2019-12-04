from model.EmployeeM import Employee
import string

class Employee_LL():
    def __init__(self):
        # self.__IOAPI = IOAPI()
        # self.__name = ""
        # self.__ssn= ""
        # self.__phone_number = "" 
        # self.__user_name = ""
        # self.__rank = ""
        self.__permit = ""
        self.__status = "At work"

    def validate_name(self,name):
        """Checks if name is valid and returns an error message if its not"""
        name = name.split()
        for elements in name:
            for letter in elements:
                if letter.isdigit() or letter in string.punctuation:
                    self.error_message(name)
        self.__name = name

    def validate_ssn(self,ssn):
        """Checks if the ssn is valid. Returns an error message if it is not"""
        if type(ssn) == int and len(str(ssn)) == 10:
            self.__ssn = ssn
        else:
            self.error_message(ssn)

    def validate_phone_number(self,phone_number):
        """Checks if the phone number is valid. Returns an error message if it is not"""
        if type(phone_number) == int and len(str(phone_number)) == 7:
            print("mamma")
        else:
            self.error_message(phone_number)

    def validate_user_name(self,user_name):
        """Checks if the user name is valid. Returns an error message if it is not"""
        if len(user_name) >= 4:
            self.__user_name = user_name
        else: 
            self.error_message(user_name)
    
    def validate_rank(self,rank):
        """Checks if the rank is valid, else it returns an error message"""
        if rank.lower() == "flight attendant" or rank.lower() == "flight service manager" \
            or rank.lower() == "co-pilot" or rank.lower() == "captain":
            self.__rank = rank
        else:
            self.error_message
    
    def validate_permit(self,permit):
        if permit != "":
            self.__permit = permit #DONT KNOW WHAT TO VALIDATE HERE. DONT REALLY KNOW WhAT PERMITS YOU CAN HAVE
    
    def validate_status(self,status):
        if self.__status != status: 
            #valid check
            self.__status = status
            pass

    def add_employee(self):
        pass

    def change_employee(self):
        pass

    def error_message(self,Error):
        return "{} is invalid".format(Error)
