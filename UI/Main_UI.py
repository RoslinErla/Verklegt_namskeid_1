from UI.Airplane_UI import AirplaneUI
# from UI.Destination_UI import DestinationUI
from UI.Employee_UI import EmployeeUI
from UI.Voyage_UI import VoyageUI

class MainUI():
    def __init__(self):
        self.airplaneui = AirplaneUI()
        # self.destinationui = DestinationUI()
        # self.employeeui = Employee_UI()
        self.voyageui = VoyageUI()

    def main_menu(self):
        action = ""
        while True:
            print("\tChange Airplane Menu")
            print()
            print('The following actions are possible:')
            print('\t1. Open Airplane Menu.')
            print('\t2. Open Destination Menu.')
            print('\t3. Open Employee Menu.')
            print('\t4. Open Voyage Menu.')

            print('Enter "q" to quit the program')
            
            action = input("Please enter your command: ")
            
            action = action.lower()

            if action == "1":
                self.airplaneui.airplane_menu()
            if action == "2":
                pass
                # self.destinationui.destination_menu()
            if action == "3":
                self.employee.employee_menu()
            if action == "4":
                pass
                self.voyageui.voyage_menu()
            if action == "q":
                break