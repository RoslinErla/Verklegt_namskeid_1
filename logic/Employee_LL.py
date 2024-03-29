from model.employeeM import Employee
from IO.employeeIO import EmployeeIO
import string

class EmployeeLL():
    def __init__(self):
        self.__employee = EmployeeIO()
    
    def check_for_ssn(self, check):
        employee_set = self.__employee.get_set()
        for elements in employee_set:
            if check == elements:
                return True

    def check_if_ssn_exists(self, check):
        employee_set = self.__employee.get_set()
        for elements in employee_set:
            if check == elements:
                return False
        else: 
            return True

    def check_if_user_name_exists(self,check):
        user_name_set = self.__employee.get_user_name_set()
        for elements in user_name_set:
            if check == elements:
                print("This username is already being used")
                return False
        else: 
            return True

    def display_pilots_by_licence(self,plane_insignia):
        return self.__employee.display_by_licence(plane_insignia)

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

    def validate_address(self,address):
        address = address.split()
        for letter in address[0]:
            if not letter.isalpha():
                return False

        return True

    def check_if_available(self,date,rank):
        self.__employee.check_if_available_and_has_licence(date,rank)
        return str(self.__employee)

    def check_if_matches(self,date,rank):
        self.__employee.check_if_available_and_has_licence(date,rank)
        return self.__employee.get_employee_list()

    def check_if_in_available(self,date,rank,ssn):
        if ssn.upper() != "N/A":
            a = self.check_if_matches(date,rank)
            for employee in a:
                if employee.get_ssn() == ssn:
                    return True
            return False
        else: 
            return True

    def validate_user_name(self, user):
        """Checks if the user name is valid. Returns True if it is valid"""
        if self.check_if_user_name_exists(user):
            if len(user) >= 4:
                return True
            else: 
                print("The user name has to be longer than or equal to 4 letters")
                return False
        else:
            return False
    
    def validate_rank(self, rank):
        """Checks if the rank is valid. Returns True if it is valid"""
        if rank.lower() == "flight attendant" or rank.lower() == "flight service manager" \
        or rank.lower() ==  "co-pilot" or rank.lower() == "captain":
            return True

    def validate_permit(self,permit):
        if permit == "N/A" or permit == "n/a" :
            return True

        for letter in permit:
            if not letter.isalpha() and not letter.isdigit():
                return False
        return True

    def add_employee(self,value_string):
        ssn,name,address,phone_number,user_name,rank,permits= value_string.split(",")
        self.__employee.Add_employee_to_file(ssn,name,address,phone_number,user_name,rank,permits)

    def change_employee(self, ssn, change, new):
        self.__employee.change_employee(ssn, change, new)

    def display_pilots(self, a):
        self.__employee.display_pilots(a)
        return str(self.__employee)
    
    def sort_employees_by_alpha(self):
        self.__employee.load_employee_from_file("alpha")
        return str(self.__employee)

    def show_by_status(self, a):
        self.__employee.display_status(a)
        return str(self.__employee)

    def show_flight_atendants(self):
        self.__employee.display_flight_attendants()
        return str(self.__employee)

    def show_single_employee(self, ssn):
        self.__employee.display_one_employee(ssn)
        return str(self.__employee)