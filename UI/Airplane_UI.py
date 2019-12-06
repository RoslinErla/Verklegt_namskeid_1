#from logic.Airplane_LL import AirplaneLL

class AirplaneUI:
    def __init__(self):
        self.airplanell = AirplaneLL()
    def airplane_menu(self):
        action = ""
        while action != "b" or action != "q":
            print("\tAirplane menu")
            print()
            print('The following actions are possible:')
            print('\t1. enter "1" to create a new plane within the system.')
            print('\t2. enter "2" to change planes already within the system.')
            print('\t3. enter "3" to display planes within the system.')
            print('Enter "b" to go back and "q" to got to the main menu.')

            action = input("Please enter your command: ").lower()

            if action == "1":
                new_plane = self.create_plane()

    def create_plane(self):
        new_plane = []
        while not self.airplanell.validate_manufacturer(input("Enter the manufacturer: ").lower()):
            print("Input is invalid")
            
        type_ID = self.__airplanell(input("Enter the type ID: ").lower())
        while type_ID.validate_typeID == False:
            print("{} is invalid").format(type_ID)
            type_ID = input("Enter the type ID: ").lower()

        plane_insignia = self.__airplanell(input("Enter the plane insignia: ").lower())
        while plane_insignia.validate_plane_insignia == False:
            print("{} is invalid").format(plane_insignia)
            plane_insignia = input("Enter the plane insignia: ").lower()

        model = self.__airplanell(input("Enter the model: ").lower())
        while model.validate_model == False:
            print("{} is invalid").format(model)
            model = input("Enter the model: ").lower()
        create_plane(manufacturer, type_ID, plane_insignia, model)
        return new_plane