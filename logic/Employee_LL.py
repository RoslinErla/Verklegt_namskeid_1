from model.employeeM import Employee
from IO.employeeIO import EmployeeIO
import string

class EmployeeLL():
    def __init__(self):
        self.__employee = EmployeeIO()
    
    def check_if_ssn_exists(self, check):
        employee_set = self.__employee.get_set()
        for elements in employee_set:
            if check == elements:
                print("This ssn already exists press 'b' to go back")
                return False
        
        else: 
            return True


    def validate_name(self,name):
        """Checks if name is valid and Returns True if it is valid"""
        name = name.split()
        for elements in name:
            for letter in elements:
                if not letter.isalpha():
                    return False
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
        if rank.lower() == ("flight attendant" or "flight service manager" or "co-pilot" or "captain"):
            return True

    def validate_status(self,status):
        if status == ("at work" or "not at work" or "on vacation"): 
            return True
        else: 
            return False

    def validate_permit(self,permit):
        if permit == ("N/A" or "n/a") :
            return True

        for letter in permit:
            if not letter.isalpha() and not letter.isdigit():
                return False
        return True

    def add_employee(self,value_string):
        ssn,name,address,phone_number,user_name,rank,permits,status = value_string.split(",")
        self.__employee.Add_employee_to_file(ssn,name,address,phone_number,user_name,rank,permits,status)

    def change_employee(self):
        pass
