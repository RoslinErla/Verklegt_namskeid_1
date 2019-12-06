from model.employeeM import Employee
import string

class EmployeeLL():
    def __init__(self):
        #TENGSL VIÐ IO
        self.__name = ""
        self.__ssn= ""
        self.__phone_number = "" 
        self.__user_name = ""
        self.__rank = ""
        self.__permit = ""
        self.__status = "At work"

    def validate_name(self,name):
        """Checks if name is valid and Returns True if it is valid"""
        name2 = self.__name.split()
        for elements in name2:
            for letter in elements:
                if letter.isdigit() or letter in string.punctuation:
                    return False
        self.__name = name
        return True

    def validate_ssn(self,ssn):
        """Checks if the ssn is valid. Returns True if it is valid"""
        try: 
            int(ssn)

        except ValueError:
            return False

        if len(ssn) == 10:
            self.__ssn = ssn
            return True

    def validate_phone_number(self, phone_number):
        """Checks if the phone number is valid. Returns True if it is valid"""
        try: 
            int(phone_number)
        except ValueError: 
            return False

        if len(phone_number) == 7:
            self.__phone_number = phone_number
            return True

    def validate_user_name(self, user):
        """Checks if the user name is valid. Returns True if it is valid"""
        if len(user) >= 4:
            self.__user_name = user
            return True
    
    def validate_rank(self, rank):
        """Checks if the rank is valid. Returns True if it is valid"""
        if rank.lower() == "flight attendant" or rank.lower() == "flight service manager" \
            or rank.lower() == "co-pilot" or rank.lower() == "captain":
            self.__rank = rank
            return True

    def validate_status(self,status):
        if self.__status != status: 
            if status == ("not at work" or "on vacation"): 
                self.__status = status
                return True

    def validate_permit(self,permit):
        for letter in permit:
            if not letter.isalpha() and not letter.isdigit():
                return False
        self.__permit = permit
        return True

    def add_employee(self):
        pass

    def change_employee(self):
        pass
