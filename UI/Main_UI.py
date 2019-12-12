from UI.Airplane_UI import AirplaneUI
from UI.Employee_UI import EmployeeUI
from UI.Voyage_UI import VoyageUI

class MainUI():
    def __init__(self):
        self.airplaneui = AirplaneUI()
        self.employeeui = EmployeeUI()
        self.voyageui = VoyageUI()

    def main_menu(self):
        action = ""
        while True:
            print("\tMain Menu")
            print()
            print('The following actions are possible:')
            print('\t1. Open Airplane Menu.')
            print('\t2. Open Employee Menu.')
            print('\t3. Open Voyage Menu.')

            print('Enter "q" to quit the program')
            
            action = input("Please enter your command: ")
            
            action = action.lower()

            if action == "1":
                self.airplaneui.airplane_menu()
            if action == "2":
                self.employeeui.employee_menu()
            if action == "3":
                self.voyageui.voyage_menu()
            if action == "q":
                break