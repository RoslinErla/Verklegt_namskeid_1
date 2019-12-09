from logic.Employee_LL import EmployeeLL

class EmployeeUI():
    
    def __init__(self):
        self.employeell = EmployeeLL()
    
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
                pass
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
            action = input("Enter the model: ")
            while not self.employeell.validate_model(action):
                print("Input is invalid!")
                action = input("Enter the model: ")
            new_employee += action + ","
            if action == 'b':
                break
            if action == 'q':
                return 'q'
            self.employeell.create_employee(new_employee)

        def call_on_validate_and_change(self):
            action = ""
            changed_employee = ""
            print("\tChange Airemployee Menu")
            print()
            print('The following actions are possible:')
            print('\t1. Create a new employee within the system.')
            print('\t2. Change employees already within the system.')
            print('\t3. Display employees within the system.')
            print('Enter "b" to go back and "q" to got to the main menu.')

            sub_action = input("Please enter your command: ")

            while sub_action == 1 and (action != "b" or action != "B"):
                action = input("Enter the manufacturer: ")
                while not self.employeell.validate_manufacturer(action):
                    print("Input is invalid!")
                    action = input("Enter the manufacturer: ")
                changed_employee += action + ","
                if action == "b":
                    break
                if action == 'q':
                    return 'q'

                action = input("Enter the type ID: ")
                action = action
                while not self.employeell.validate_typeID(action):
                    print("Input is invalid!")
                    action = input("Enter the type ID: ")
                changed_employee += action + ","
                if action == "b":
                    break
                if action == 'q':
                    return 'q'

                action = input("Enter the phone number: ")
                while not self.employeell.validate_employee_insignia(action):
                    print("Input is invalid!")
                    action = input("Enter the phone number: ")
                changed_employee += action + ","
                if action == "b":
                    break
                if action == 'q':
                    return 'q'

                action = input("Enter the model: ")
                while not self.employeell.validate_model(action):
                    print("Input is invalid!")
                    action = input("Enter the model: ")
                changed_employee += action + ","
                if action == "b":
                    break
                if action == 'q':
                    return 'q'

                change_employee = self.employeell.change_employee(new_employee)
                break