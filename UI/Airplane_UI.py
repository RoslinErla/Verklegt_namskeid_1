from logic.Airplane_LL import AirplaneLL

class AirplaneUI:
    def __init__(self):
        self.airplanell = AirplaneLL()
    def airplane_menu(self):
        action = ""
        if action != "b" or action != "q":
            print("\tAirplane Menu")
            print()
            print('The following actions are possible:')
            print('\t1. enter "1" to create a new plane within the system.')
            print('\t2. enter "2" to change planes already within the system.')
            print('\t3. enter "3" to display planes within the system.')
            print('Enter "b" to go back and "q" to got to the main menu.')

            action = input("Please enter your command: ")
            action = action.lower()
            if action == "1":
                self.call_on_validate_and_create()
            if action == "2":
                self.call_on_validate_and_change()
            if action == "3":
                pass
            if action == "b":
                break

    def call_on_validate_and_create(self):
        action = ""
        new_plane = []
        if action != "b" or action != "B":
            action = input("Enter the manufacturer: ")
            while not self.airplanell.validate_manufacturer(action):
                print("Input is invalid")
                action = input("Enter the manufacturer: ")
            new_plane.append(action)

            action = input("Enter the type ID: ")
            action = action
            while not self.airplanell.validate_typeID(action):
                print("Input is invalid")
                action = input("Enter the type ID: ")
            new_plane.append(action)

            action = input("Enter the plane insignia: ")
            while not self.airplanell.validate_plane_insignia(action):
                print("Input is invalid")
                action = input("Enter the plane insignia: ")
            new_plane.append(action)

            action = input("Enter the model: ")
            while not self.airplanell.validate_model(action):
                print("Input is invalid")
                action = input("Enter the model: ")
            new_plane.append(action)
            new_plane = self.airplanell.create_plane(new_plane)
            action = "b"

        def call_on_validate_and_change(self):
            action = ""
            changed_plane = []
            print("\tChange Airplane Menu")
            print()
            print('The following actions are possible:')
            print('\t1. enter "1" to create a new plane within the system.')
            print('\t2. enter "2" to change planes already within the system.')
            print('\t3. enter "3" to display planes within the system.')
            print('Enter "b" to go back and "q" to got to the main menu.')

            sub_action = input("Please enter your command: ")

            if sub_action == 1 and (action != "b" or action != "B"):
                action = input("Enter the manufacturer: ")
                while not self.airplanell.validate_manufacturer(action):
                    print("Input is invalid")
                    action = input("Enter the manufacturer: ")
                changed_plane.append(action)

                action = input("Enter the type ID: ")
                action = action
                while not self.airplanell.validate_typeID(action):
                    print("Input is invalid")
                    action = input("Enter the type ID: ")
                change_plane.append(action)

                action = input("Enter the plane insignia: ")
                while not self.airplanell.validate_plane_insignia(action):
                    print("Input is invalid")
                    action = input("Enter the plane insignia: ")
                change_plane.append(action)

                action = input("Enter the model: ")
                while not self.airplanell.validate_model(action):
                    print("Input is invalid")
                    action = input("Enter the model: ")
                change_plane.append(action)
                
                change_plane = self.airplanell.change_plane(new_plane)
                action = "b"