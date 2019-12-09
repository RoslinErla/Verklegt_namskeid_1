from model.employeeM import Employee
from IO.employeeIO import EmployeeIO
import string

class EmployeeLL():
    def __init__(self):
        self.__employee = EmployeeIO()
    
    def check_if_ssn_exists(self, check):
        employee_list = self.__employee.get_employee_list()
        for lists in employee_list:
            if check in lists:
                return False
        
        else: 
            return True


    def validate_name(self,name):
        """Checks if name is valid and Returns True if it is valid"""
        name = name.split()
        for elements in name:
            for letter in elements:
                if letter.isdigit() or letter in string.punctuation:
                    return False
        self.__name = name
        return True

    def validate_ssn(self,ssn):
        """Checks if the ssn is valid. Returns True if it is valid"""
        if self.check_if_ssn_exists(ssn):
            try: 
                int(ssn)

            except ValueError:
                return False

            if len(ssn) == 10:
                return True

    def validate_phone_number(self, phone_number):
        """Checks if the phone number is valid. Returns True if it is valid"""
        try: 
            int(phone_number)
        except ValueError: 
            return False

        if len(phone_number) == 7:
            return True

    def validate_user_name(self, user):
        """Checks if the user name is valid. Returns True if it is valid"""
        if len(user) >= 4:
            return True
    
    def validate_rank(self, rank):
        """Checks if the rank is valid. Returns True if it is valid"""
        if rank.lower() == "flight attendant" or rank.lower() == "flight service manager" \
            or rank.lower() == "co-pilot" or rank.lower() == "captain":
            self.__rank = rank
            return True

    def validate_status(self,status):
        if status != "At work": 
            if status == ("not at work" or "on vacation"): 
                return True
        else: 
            return True

    def validate_permit(self,permit):
        for letter in permit:
            if not letter.isalpha() and not letter.isdigit():
                return False
        return True

    def add_employee(self):
        pass

    def change_employee(self):
        pass
