from model.AirplaneM import Airplane
from logic.Airplane_LL import AirplaneLL

class AirplaneUI:
    def __init__(self, inp):
        self.__inp = inp

    def airplane_menu(self):
        action = ""
        while action != "b" or action != "q":
            print("\tAirplane meanu")
            print()
            print("""The following actions are possible:""")
            print("""\t1. enter "1" to create a new plane within the system.""")
            print("""\t2. enter "2" to change planes already within the system.""")
            print("""\t3. enter "3" to show planes within the system.""")
            print("""Enter "b" to go back and "q" to got to the main menu.""")

            action = input("Please enter your command").lower()

            if action == 1:
                manufacturer = input("Enter the manufacturer: ")
                type_ID = input("Enter the type ID: ")
                plane_insignia = input("Enter the plane insignia: ")
                model = input("Enter the model:")
