from UI.Airplane_UI import AirplaneUI

class MainUI():
    def __init__(self):
        self.airplaneui = AirplaneUI()
    
    def main_menu(self):
        action = ""
        while True:
            print("\tChange Airplane Menu")
            print()
            print('The following actions are possible:')
            print('\t1. Open Airplane Menu.')
            print('\t2. Open Voyage Menu.')
            print('\t3. Open Employee Menu.')
            print('Enter "q" to quit the program')
            
            action = input("Please enter your command: ")
            
            action = action.lower()

            if action == "1":
                self.airplaneui.airplane_menu()
            if action == "2":
                self.call_on_validate_and_change()
            if action == "3":
                pass
            if action == "q":
                break