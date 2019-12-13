from UI.Airplane_UI import AirplaneUI
from UI.Destination_UI import DestinationUI
from UI.Employee_UI import EmployeeUI
from UI.Voyage_UI import VoyageUI
from UI.frame import Frame

class MainUI():
    def __init__(self):
        self.airplaneui = AirplaneUI()
        self.destinationui = DestinationUI()
        self.employeeui = EmployeeUI()
        self.voyageui = VoyageUI()
        self.frame = Frame()

    def main_menu(self):
        """ Presents the user with the option to open any menu within the system """
        action = ""
        while True:
            print("\tMain Menu")
            print()
            print('The following actions are possible:')
            print('\t1. Open Airplane Menu.')
            print('\t2. Open Destination Menu.')
            print('\t3. Open Employee Menu.')
            print('\t4. Open Voyage Menu.')

            print('Enter "q" to quit the program')
            
            action = input("Please enter your command: ")
            
            action = action.lower()
            self.frame.delete_line(100)
            
            if action == "1":
                self.airplaneui.airplane_menu()
            if action == "2":
                self.destinationui.destination_menu()
            if action == "3":
                self.employeeui.employee_menu()
            if action == "4":
                self.voyageui.voyage_menu()
            if action == "q":
                break
            