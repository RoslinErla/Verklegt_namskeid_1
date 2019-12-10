from IO.airplaneIO import AirplaneIO
from logic.Airplane_LL import AirplaneLL


class AirplaneUI:
    def __init__(self):
        self.airplanell = AirplaneLL()
        self.airplaneio = AirplaneIO()
    def airplane_menu(self):
        action = ""
        leave = ''
        while leave != "q":
            print("\tAirplane Menu")
            print()
            print('The following actions are possible:')
            print('\t1. enter "1" to create a new plane within the system.')
            print('\t2. enter "2" to change planes already within the system.')
            print('\t3. enter "3" to display planes within the system.')
            print('Enter "b" to go back and "q" to got to the main menu.')

            action = input("Please enter your command: ")
            print()

            action = action.lower()

            if action == "1":
                leave = self.call_on_validate_and_create()
            if action == "2":
                leave = self.call_on_validate_and_change()
            if action == "3":
                leave = self.show()
            if action == "b" or action == "q":
                break

    def call_on_validate_and_create(self):
        print('Enter "b" to go back and "q" to got to the main menu.')
        action = ""
        new_plane = ""
        while True:
            action = input("Enter the manufacturer: ")
            while not self.airplanell.validate_manufacturer(action):
                print("Input is invalid!")
                action = input("Enter the manufacturer: ")
            new_plane += action + ","
            if action == 'b':
                break
            elif action == 'q':
                return 'q'
            action = input("Enter the type ID: ")
            while not self.airplanell.validate_typeID(action):
                print("Input is invalid!")
                action = input("Enter the type ID: ")
            new_plane += action + ","
            if action == 'b':
                break
            if action == 'q':
                return 'q'
            action = input("Enter the plane insignia: ")
            while not self.airplanell.validate_plane_insignia(action):
                print("Input is invalid!")
                action = input("Enter the plane insignia: ")
            new_plane += action + ","
            if action == 'b':
                break
            if action == 'q':
                return 'q'
            action = input("Enter the model: ")
            while not self.airplanell.validate_model(action):
                print("Input is invalid!")
                action = input("Enter the model: ")
            new_plane += action + ","
            if action == 'b':
                break
            if action == 'q':
                return 'q'
            self.airplanell.create_plane(new_plane)
            action = input("Do you want to create another airplane? (y)es or (n)o: " ).lower()
            if action == "n":
                action = "q"

    def call_on_validate_and_change(self):
        while True:
            self.airplaneio.load_airplane_from_file()
            print(self.airplaneio)
            print()
            planeinsignia = input("Please enter the Plane Insignia of the employee who's information you want to edit: ")
            if planeinsignia == "q":
                return "q"
            if planeinsignia == "b":
                break
            change = input("Please enter what you wish to change: ")
            if change == "q":
                return "q"
            if change == "b":
                break
            new = input("Please enter the new entry for {}".format(change))
            if new == "q":
                return "q"
            if new == "b":
                break
            print()
            self.airplanell.change_airplane(plane_insignia, change, new)
            action = input("Do you want to change another airplane? (y)es or (n)o: " ).lower()
            if action == "n":
                action = "q"
        
    
    def show(self):
        print()
        self.airplaneio.load_airplane_from_file()
        print(self.airplaneio)
        print()