from logic.Airplane_LL import AirplaneLL


class AirplaneUI:
    def __init__(self):
        self.airplanell = AirplaneLL()
    def airplane_menu(self):
        action = ""
        leave = ''
        while action != "b" and leave != "q":
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
                leave = self.call_on_validate_and_create()
            if action == "2":
                self.call_on_validate_and_change()
            if action == "3":
                pass
            if action == "b" or action = "q":
                break

    def call_on_validate_and_create(self):
        print('Enter "b" to go back and "q" to got to the main menu.')
        action = ""
        new_plane = ""
        while action.lower() != 'q':
            action = input("Enter the manufacturer: ")
            while not self.airplanell.validate_manufacturer(action):
                print("Input is invalid")
                action = input("Enter the manufacturer: ")
            new_plane += action + ","
            if action == 'b':
                break
            elif action == 'q':
                return 'q'
            action = input("Enter the type ID: ")
            while not self.airplanell.validate_typeID(action):
                print("Input is invalid")
                action = input("Enter the type ID: ")
            new_plane += action + ","
            if action == 'b':
                break
            if action == 'q':
                main_menu()
            action = input("Enter the plane insignia: ")
            while not self.airplanell.validate_plane_insignia(action):
                print("Input is invalid")
                action = input("Enter the plane insignia: ")
            new_plane += action + ","
            if action == 'b':
                break
            if action == 'q':
                self.mainui.main_menu()
            action = input("Enter the model: ")
            while not self.airplanell.validate_model(action):
                print("Input is invalid")
                action = input("Enter the model: ")
            new_plane += action + ","
            if action == 'b':
                break
            if action == 'q':
                self.main_menu()
            self.airplanell.create_plane(new_plane)

        def call_on_validate_and_change(self):
            action = ""
            changed_plane = ""
            print("\tChange Airplane Menu")
            print()
            print('The following actions are possible:')
            print('\t1. Create a new plane within the system.')
            print('\t2. Change planes already within the system.')
            print('\t3. Display planes within the system.')
            print('Enter "b" to go back and "q" to got to the main menu.')

            sub_action = input("Please enter your command: ")

            while sub_action == 1 and (action != "b" or action != "B"):
                action = input("Enter the manufacturer: ")
                while not self.airplanell.validate_manufacturer(action):
                    print("Input is invalid")
                    action = input("Enter the manufacturer: ")
                changed_plane += action + ","
                if action == "b":
                    break
                if action == 'q':
                    self.mainui.main_menu()

                action = input("Enter the type ID: ")
                action = action
                while not self.airplanell.validate_typeID(action):
                    print("Input is invalid")
                    action = input("Enter the type ID: ")
                changed_plane += action + ","
                if action == "b":
                    break
                if action == 'q':
                    self.mainui.main_menu()

                action = input("Enter the plane insignia: ")
                while not self.airplanell.validate_plane_insignia(action):
                    print("Input is invalid")
                    action = input("Enter the plane insignia: ")
                changed_plane += action + ","
                if action == "b":
                    break
                if action == 'q':
                    self.mainui.main_menu()

                action = input("Enter the model: ")
                while not self.airplanell.validate_model(action):
                    print("Input is invalid")
                    action = input("Enter the model: ")
                changed_plane += action + ","
                if action == "b":
                    break
                if action == 'q':
                    self.mainui.main_menu()

                change_plane = self.airplanell.change_plane(new_plane)
                break