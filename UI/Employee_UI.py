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
            print('\t3. enter "3" to display employees within the system.')
            print('Enter "b" to go back and "q" to got to the main menu.')

            action = input("Please enter your command: ")
            
            action = action.lower()

            if action == "1":
                leave = self.call_on_validate_and_create()
            if action == "2":
                leave =  self.call_on_validate_and_change()
            if action == "3":
                self.show_by_status()
            if action == "b" or action == "q":
                break

    def call_on_validate_and_create(self):
        print('Enter "b" to go back and "q" to got to the main menu.')
        action = ""
        new_employee = ""
        while action.lower() != 'q':
            action = input("Enter the name: ")
            while not self.employeell.validate_name(action):
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
            new_employee += action + ","
            if action == 'b':
                break
            if action == 'q':
                return 'q'
            action = input("Enter the rank: ")
            while not self.employeell.validate_rank(action):
                print("Input is invalid!")
                action = input("Enter the rank: ")
            new_employee += action + ","
            if action == 'b':
                break
            if action == 'q':
                return 'q'
            action = input("Enter the permit, if appropiet: ")
            while not self.employeell.validate_permit(action):
                print("Input is invalid!")
                action = input("Enter the permit, if appropiet: ")
            new_employee += action + ","
            if action == 'b':
                break
            if action == 'q':
                return 'q'
            self.employeell.add_employee(new_employee)

    def call_on_validate_and_change(self):
        action = ""
        changed_employee = ""
        print("\tChange Employee Menu")
        print()
        print('The following actions are possible:')
        print('\t1. Create a new employee within the system.')
        print('\t2. Change employees already within the system.')
        print('\t3. Display employees within the system.')
        print('Enter "b" to go back and "q" to got to the main menu.')
        print('Enter "b" to go back and "q" to got to the main menu.')
        while action.lower() != 'q':
            action = input("Enter the name: ")
            while not self.employeell.validate_name(action):
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
            new_employee += action + ","
            if action == 'b':
                break
            if action == 'q':
                return 'q'
            action = input("Enter the rank: ")
            while not self.employeell.validate_rank(action):
                print("Input is invalid!")
                action = input("Enter the rank: ")
            new_employee += action + ","
            if action == 'b':
                break
            if action == 'q':
                return 'q'
            action = input("Enter the permit, if appropiet: ")
            while not self.employeell.validate_permit(action):
                print("Input is invalid!")
                action = input("Enter the permit, if appropiet: ")
            new_employee += action + ","
            if action == 'b':
                break
            if action == 'q':
                return 'q'
            sub_action = input("Please enter your command: ")
            change_employee = self.employeell.change_employee(new_employee)
            break
    def show_by_status(self):
        self.employeeio.load_employee_from_file("status")