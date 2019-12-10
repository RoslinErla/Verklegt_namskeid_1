from IO.employeeIO import EmployeeIO
from logic.Employee_LL import EmployeeLL

class EmployeeUI():
    
    def __init__(self):
        self.employeell = EmployeeLL()
        self.employeeio = EmployeeIO()

    def employee_menu(self):
        action = ""
        leave = ''
        while action != "b" and leave != "q":
            print("\tEmployee Menu")
            print()
            print('The following actions are possible:')
            print('\t1. enter "1" to create a new employee within the system.')
            print('\t2. enter "2" to change employees already within the system.')
            print('\t3. enter "3" to display employees within the system by their status.')
            print('\t4. enter "4" to display employees within the system in alphabetical order.')
            print('Enter "b" to go back and "q" to got to the main menu.')

            action = input("Please enter your command: ")
            print()

            action = action.lower()

            if action == "1":
                leave = self.call_on_validate_and_create()
            if action == "2":
                leave =  self.call_on_validate_and_change()
            if action == "3":
                self.show_by_status()
            if action == "4":
                self.show_by_aplha()
            if action == "b" or action == "q":
                break

    def call_on_validate_and_create(self):
        print('Enter "b" to go back and "q" to got to the main menu.')
        action = ""
        new_employee = ""
        while action.lower() != 'q':
            action = input("Enter the ssn: ")
            while not self.employeell.validate_ssn(action):
                print("Input is invalid!")
                action = input("Enter the name: ")
            new_employee += action + ","
            if action == 'b':
                break
            elif action == 'q':
                return 'q'
            action = input("Enter the ssn: ")
            while not self.employeell.validate_ssn(action):
                print("Input is invalid!")
                action = input("Enter the ssn: ")
            new_employee += action + ","

            if action == 'b':
                break
            if action == 'q':
                return 'q'

            action = input("Enter the address: ")
            while not self.employeell.validate_address(action):
                print("input is invalid!")
                action = input("Enter the address")
            new_employee += action +","
            action = input("Enter the phone number: ")
            while not self.employeell.validate_phone_number(action):
                print("Input is invalid!")
                action = input("Enter the phone number: ")
            new_employee += action + ","
            if action == 'b':
                break
            if action == 'q':
                return 'q'
            action = input("Enter the user name: ")
            while not self.employeell.validate_user_name(action):
                print("Input is invalid!")
                action = input("Enter the user name: ")
                if action == 'b':
                    break
                if action == 'q':
                    return 'q'
            new_employee += action + ","

            if action == 'b':
                break
            if action == 'q':
                return 'q'
            action = input("Enter the rank: ")
            while not self.employeell.validate_rank(action):
                print("Input is invalid!")
                action = input("Enter the rank: ")
                if action == 'b':
                    break
                if action == 'q':
                    return 'q'
                
            new_employee += action + ","
            if action == 'b':
                break
            if action == 'q':
                return 'q'
            action = input("Enter the permit, enter N/A if not appropriate: ")
            while not self.employeell.validate_permit(action):
                print("Input is invalid!")
                action = input("Enter the permit, enter N/A if not appropriate: ")
            new_employee += action + ","
            action = input("Enter the status of the employee (at work, not at work, on vacation): ")
            while not self.employeell.validate_status(action):
                print("input is invalid")
                action = input("Enter the status")
            new_employee += action

            if action == 'b':
                break
            if action == 'q':
                return 'q'

            self.employeell.add_employee(new_employee)

            action = input("Do you want to create a new employee? (y)es or (n)o: " ).lower()
            if action == "n":
                action = "q"


    def call_on_validate_and_change(self):
        while True:
            self. employeeio.load_employee_from_file("alpha")
            print(self.employeeio)
            print()
            ssn = input("Please enter the SSN of the employee who's information you want to edit: ")
            if ssn == "q":
                return "q"
            if ssn == "b":
                break
            change = input("Please enter what you wish to change: ")
            if change == "q":
                return "q"
            if change == "b":
                break
            new = input("Please enter the new entry for {}".format(change))
            if new == "q":
                return "q"
            if new == "b":
                break
            print()
            self.employeell.change_employee(ssn, change, new)

            action = input("Do you want to change another employee? (y)es or (n)o: " ).lower()
            if action == "n":
                action = "q"
    
    def show_by_status(self):
        print()
        self.employeeio.load_employee_from_file("status")
        print(self.employeeio)
        print()
    
    def show_by_aplha(self):
        print()
        self. employeeio.load_employee_from_file("alpha")
        print(self.employeeio)
        print()