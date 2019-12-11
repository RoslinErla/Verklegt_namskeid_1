from IO.employeeIO import EmployeeIO
from logic.Employee_LL import EmployeeLL
import datetime

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
            print("\t5. enter '5' to display all flight attendants within the system. ")
            print("\t6. enter '6' to display all pilots within the system. ")
            print("\t7. enter '7' to display all information about a employee. ")
            print('Enter "b" to go back and "q" to got to the main menu.')

            action = input("Please enter your command: ")
            print()

            action = action.lower()

            if action == "1":
                leave = self.call_on_validate_and_create()
            elif action == "2":
                leave =  self.call_on_validate_and_change()
            elif action == "3":
                self.show_by_status()
            elif action == "4":
                self.show_by_aplha()
            elif action == "5":
                self.show_by_rank("flight attendant")
            elif action == "6":
                self.show_by_rank("pilot")
            elif action == "7":
                self.show_a_single_employee()
            elif action == "b" or action == "q":
                break

    def call_on_validate_and_create(self):
        print('Enter "b" to go back and "q" to got to the main menu.')
        action = ""
        new_employee = ""
        while action.lower() != 'q':
            action = input("Enter the ssn: ")
            while not self.employeell.validate_ssn(action):
                print("Input is invalid!")
                action = input("Enter the ssn: ")
                if action == 'b':
                    break
                elif action == 'q':
                    return 'q'
            
            if action == 'b':
                break
            elif action == 'q':
                return 'q'

            new_employee += action + ","

            action = input("Enter the name: ")
            while not self.employeell.validate_name(action):
                print("Input is invalid!")
                action = input("Enter the name: ")
                if action == 'b':
                    break
                if action == 'q':
                    return 'q'

            new_employee += action + ","

            if action == 'b':
                break
            if action == 'q':
                return 'q'

            action = input("Enter the address: ")
            while not self.employeell.validate_address(action):
                print("input is invalid!")
                action = input("Enter the address")
                if action == 'b':
                    break
                elif action == 'q':
                    return 'q'
    
            new_employee += action + ","

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

            action = input("Enter the rank (flight attendant, flight service manager, co-pilot or captain): ")
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
                if action == 'b':
                    break
                if action == 'q':
                    return 'q'

            new_employee += action + ","
            if action == 'b':
                break
            if action == 'q':
                return 'q'

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
                return "q"


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
            print("Enter '1' to change the name. ")
            print("Enter '2' to change the address. ")
            print("Enter '3' to change the phone_number. ")
            print("Enter '4' to change the user_name. ")
            print("Enter '5' to change the rank. ")
            print("Enter '6' to change the permit. ")
            print("Enter '7' to change the status. ")
            print("Enter 'q' to go back to the main menu")
            print("Enter 'b' to go back to the employee menu")

            action = input("Please enter your command: ")

            if action == "b":
                break
            elif action == "q":
                return "q"
            elif action == "1":
                change = "name"
                if change == "q":
                    return "q"
                if change == "b":
                    break
                new = input("please enter the new entry for {}: ".format(change))
                while not self.employeell.validate_status(new):
                    print("input is invalid")
                    new = input("Enter the status")
                    

            elif action == "2":
                change = "address"
                new = input("please enter the new entry for {}: ".format(change))
            elif action == 
            

            change = input("you can change: name, phone_number, Please enter what you wish to change: ")
            
            new = input("Please enter the new entry for {}: ".format(change))
            if new == "q":
                return "q"
            if new == "b":
                break
            print()
            self.employeell.change_employee(ssn, change, new)

            action = input("Do you want to change another employee? (y)es or (n)o: " ).lower()
            if action == "n":
                return "q"
    
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

    def show_by_rank(self,rank):
        print()
        if rank == "pilot":
            self.employeeio.display_pilots()
            print(self.employeeio)
            print()

        if rank == "flight attendant":
            self.employeeio.display_flight_attendants()
            print(self.employeeio)
            print()

    def show_a_single_employee(self):
        self.employeeio.load_employee_from_file("alpha")
        print(self.employeeio)
        ssn = input("enter the ssn of the employee you want to see: ")
        self.employeeio.display_one_employee(ssn)
        print(self.employeeio)
        print()
