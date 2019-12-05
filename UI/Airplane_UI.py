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
            print('The following actions are possible:')
            print('\t1. enter "1" to create a new plane within the system.')
            print('\t2. enter "2" to change planes already within the system.')
            print('\t3. enter "3" to display planes within the system.')
            print('Enter "b" to go back and "q" to got to the main menu.')

            action = input("Please enter your command").lower()

            if action == 1:
                manufacturer = input("Enter the manufacturer: ").lower()
                type_ID = input("Enter the type ID: ").lower()
                plane_insignia = input("Enter the plane insignia: ").lower()
                model = input("Enter the model:").lower()
                if manufacturer.validate_manufacturer == True and type_ID.validate_typeID == True and plane_insignia.validate_plane_insignia:

                new 