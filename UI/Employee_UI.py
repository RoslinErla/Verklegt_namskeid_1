from logic.Employee_LL import EmployeeLL
import datetime
from UI.frame import Frame

class EmployeeUI():
    
    def __init__(self):
        self.employeell = EmployeeLL()
        self.frame = Frame()
    def employee_menu(self):
        action = ""
        leave = ''
        while action != "b" and leave != "q":
            print("\tEmployee Menu")
            print()
            print('The following actions are possible:')
            print('\t1. Enter "1" to create a new employee within the system.')
            print('\t2. Enter "2" to change employees already within the system.')
            print('\t3. Enter "3" to display employees within the system by their status.')
            print('\t4. Enter "4" to display employees within the system in alphabetical order.')
            print("\t5. Enter '5' to display all flight attendants within the system. ")
            print("\t6. Enter '6' to display all pilots within the system. ")
            print("\t7. Enter '7' to display all pilots sorted by their permits. ")
            print("\t8. Enter '8' to display all information about a employee. ")
            print('Enter "b" to go back and "q" to got to the main menu.')

            action = input("Please enter your command: ")
            print()

            action = action.lower()
            self.frame.clear_all()

            if action == "1":
                leave = self.call_on_validate_and_create()
            elif action == "2":
                leave =  self.call_on_validate_and_change()
            elif action == "3":
                leave = self.show_by_status()
            elif action == "4":
                leave = self.show_by_aplha()
            elif action == "5":
                leave = self.show_by_rank("flight attendant")
            elif action == "6":
                leave = self.show_by_rank("pilot")
            elif action =="7":
                leave = self.show_by_licence()
            elif action == "8":
                leave = self.show_a_single_employee()
            elif action == "b" or action == "q":
                break

    def call_on_validate_and_create(self):
        print('Enter "b" to go back and "q" to got to the main menu.')
        action = ""
        new_employee = ""

        self.frame.clear_all()

        while action.lower() != 'q':
            action = input("Enter the ssn: ")
            if action == 'b':
                    break
            elif action == 'q':
                return 'q'
            while not self.employeell.validate_ssn(action):
                print("Input is invalid!")
                action = input("Enter the ssn: ")
                if action == 'b':
                    break
                elif action == 'q':
                    return 'q'
            
            self.frame.clear_all()

            new_employee += action + ","

            action = input("Enter the name: ")

            if action == 'b':
                    break
            elif action == 'q':
                return 'q'
            
            self.frame.clear_all()

            while not self.employeell.validate_name(action):
                print("Input is invalid!")
                action = input("Enter the name: ")
                if action == 'b':
                    break
                if action == 'q':
                    return 'q'

            self.frame.clear_all()

            new_employee += action + ","

            action = input("Enter the address: ")
            if action == 'b':
                    break
            elif action == 'q':
                return 'q'

            self.frame.clear_all()

            while not self.employeell.validate_address(action):
                print("input is invalid!")
                action = input("Enter the address")
                if action == 'b':
                    break
                elif action == 'q':
                    return 'q'
    
            new_employee += action + ","

            self.frame.clear_all()

            action = input("Enter the phone number: ")

            if action == 'b':
                    break
            elif action == 'q':
                return 'q'
            self.frame.clear_all()

            while not self.employeell.validate_phone_number(action):
                print("Input is invalid!")
                action = input("Enter the phone number: ")
                if action == 'b':
                    break
                elif action == 'q':
                    return 'q'
                self.frame.clear_all()

            new_employee += action + ","

            action = input("Enter the user name: ")
            if action == 'b':
                    break
            elif action == 'q':
                return 'q'
            self.frame.clear_all()

            while not self.employeell.validate_user_name(action):
                print("Input is invalid!")
                action = input("Enter the user name: ")
                if action == 'b':
                    break
                if action == 'q':
                    return 'q'
            new_employee += action + ","
            self.frame.clear_all()

            action = input("Enter the rank (flight attendant, flight service manager, co-pilot or captain): ")
            
            if action == 'b':
                    break
            elif action == 'q':
                return 'q'
            self.frame.clear_all()

            while not self.employeell.validate_rank(action):
                print("Input is invalid!")
                action = input("Enter the rank: ")
                if action == 'b':
                    break
                if action == 'q':
                    return 'q'
            self.frame.clear_all()
                
            new_employee += action + ","

            action = input("Enter the permit, enter N/A if not appropriate: ")

            if action == 'b':
                    break
            elif action == 'q':
                return 'q'
            self.frame.clear_all()

            while not self.employeell.validate_permit(action):
                print("Input is invalid!")
                action = input("Enter the permit, enter N/A if not appropriate: ")
                if action == 'b':
                    break
                if action == 'q':
                    return 'q'
                self.frame.clear_all()

            new_employee += action

            self.employeell.add_employee(new_employee)

            action = input("Do you want to create a new employee? (y)es or (n)o: " ).lower()
            if action == "n":
                return "q"
            self.frame.clear_all()


    def call_on_validate_and_change(self):
        while True:
            employio = self.employeell.sort_employees_by_alpha()
            print(employio)
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
            print("Enter 'q' to go back to the main menu")
            print("Enter 'b' to go back to the employee menu")

            action = input("Please enter your command: ")
            self.frame.clear_all()

            if action == "b":
                break

            elif action == "q":
                return "q"

            elif action == "1":
                change = "name"
                action = input("please enter the new entry for {}: ".format(change))
                if action == 'b':
                    break
                elif action == 'q':
                    return 'q'
                while not self.employeell.validate_name(action):
                    print("input is invalid")
                    action = input("please enter the new entry for {}: ".format(change))
                    if action == 'b':
                        break
                    elif action == 'q':
                        return 'q'
                    self.frame.clear_all()

            elif action == "2":
                change = "address"
                action = input("please enter the new entry for {}: ".format(change))
                if action == 'b':
                    break
                elif action == 'q':
                    return 'q'
                while not self.employeell.validate_address(action):
                    print("input is invalid")
                    action = input("please enter the new entry for {}: ".format(change))
                    if action == 'b':
                        break
                    elif action == 'q':
                        return 'q'

                    self.frame.clear_all()

            elif action == "3":
                change = "phone_number"
                action = input("please enter the new entry for {}: ".format(change))
                if action == 'b':
                    break
                elif action == 'q':
                    return 'q'
                self.frame.clear_all()
                while not self.employeell.validate_phone_number(action):
                    print("input is invalid")
                    action = input("please enter the new entry for {}: ".format(change))
                    if action == 'b':
                        break
                    elif action == 'q':
                        return 'q'

                    self.frame.clear_all()

            elif action == "4":
                change = "user_name"
                action = input("please enter the new entry for {}: ".format(change))
                if action == 'b':
                    break
                elif action == 'q':
                    return 'q'

                self.frame.clear_all()

                while not self.employeell.validate_user_name(action):
                    print("input is invalid")
                    action = input("please enter the new entry for {}: ".format(change))
                    if action == 'b':
                        break
                    elif action == 'q':
                        return 'q'
                    
                    self.frame.clear_all()

            self.employeell.change_employee(ssn, change, action)

            action = input("Do you want to change another employee? (y)es or (n)o: " ).lower()
            if action == "n":
                return "q"

            self.frame.clear_all()

    
    def show_by_status(self):
        a = input("Please enter YYYY/mm/dd: ")
        if a == "b":
            self.employee_menu()
        if a == "q":
            return "q"
        print()
        b = self.employeell.show_by_status(a)
        print(b)
        action = input('Enter "b" to go back and "q" to got to the main menu: ')
        if action == "q":
            return "q"

        self.frame.clear_all()

    def show_by_aplha(self):
        print()
        employio = self.employeell.sort_employees_by_alpha()
        print(employio)
        print()
        action = input('Enter "b" to go back and "q" to got to the main menu: ')
        if action == "q":
            return "q"

        self.frame.clear_all()

    def show_by_rank(self,rank):
        print()
        if rank == "pilot":
            employio = self.employeell.display_pilots("alpha")
            print(employio)
            print()
            action = input('Enter "b" to go back and "q" to got to the main menu: ')
            if action == "q":
                return "q"

        if rank == "flight attendant":
            a = self.employeell.show_flight_atendants()
            print(a)
            print()
            action = input('Enter "b" to go back and "q" to got to the main menu: ')
            if action == "q":
                return "q"

            self.frame.clear_all()

    def show_a_single_employee(self):
        employio = self.employeell.sort_employees_by_alpha()
        print(employio)
        ssn = input("enter the ssn of the employee you want to see: ")
        if ssn == 'b':
            self.employee_menu()
        elif ssn == 'q':
            return 'q'

        self.frame.clear_all()

        while not self.employeell.check_for_ssn(ssn):
            print("Invalid input!")
            ssn = input("Enter the ssn: ")
            if ssn == 'b':
                self.employee_menu()
            if ssn == 'q':
                return 'q'
            self.frame.clear_all()

        employio = self.employeell.show_single_employee(ssn)
        print(employio)
        print()
        action = input('Enter "b" to go back and "q" to got to the main menu: ')
        if action == "q":
            return "q"
        
        self.frame.clear_all()

    def show_by_licence(self):
        print()
        employio = self.employeell.display_pilots("permit")
        print(employio)
        print()
        action = input('Enter "b" to go back and "q" to got to the main menu: ')
        if action == "q":
            return "q"
            
        self.frame.clear_all()
