from logic.Airplane_LL import AirplaneLL



class AirplaneUI:
    def __init__(self):
        self.airplanell = AirplaneLL()
    
    def airplane_menu(self):
        ''' Presents the user with every interaction for "airplane_menu". '''
        action = ""
        leave = ''
        while leave != "q":
            print("\tAirplane Menu")
            print()
            print('The following actions are possible:')
            print('\t1. enter "1" to create a new plane within the system.')
            print('\t2. enter "2" to display pilots with a specific licence')
            print('\t3. enter "3" to display planes within the system.')
            print('Enter "b" to go back and "q" to got to the main menu.')

            action = input("Please enter your command: ")
            print()

            action = action.lower()
            

            if action == "1":
                leave = self.call_on_validate_and_create()
            if action == "2":
                leave = self.show_pilots_by_airplane_type()
            if action == "3":
                leave = self.show()
            if action == "b" or action == "q":
                break
            delete_line(100)

    def call_on_validate_and_create(self):
        """ Asks the user for input for each object required in  """
        print('Enter "b" to go back and "q" to got to the main menu.')
        action = ""
        new_plane = ""
        while True:
            action = input("Enter the manufacturer: ").upper()
            if action == "B":
                self.airplane_menu()
            elif action == "Q":
                return 'q'
        delete_line(100)

            while not self.airplanell.validate_manufacturer(action):
                print("Input is invalid!")
                action = input("Enter the manufacturer: ").upper()
                if action == "B":
                    self.airplane_menu()
                elif action == "Q":
                    return 'q'          
            new_plane += action + ","
            delete_line(100)


            action = input("Enter the type ID: ").upper()
            if action == "B":
                self.airplane_menu()
            elif action == "Q":
                return 'q'
            delete_line(100)

            while not self.airplanell.validate_typeID(action):
                print("Input is invalid!")
                action = input("Enter the type ID: ").upper()
                if action == "B":
                    self.airplane_menu()
                elif action == "Q":
                    return 'q'
            new_plane += action + ","
            delete_line(100)

            action = input("Enter the plane insignia: ").upper()
            if action == "B":
                    self.airplane_menu()
            elif action == "Q":
                return 'q'
            delete_line(100)

            while not self.airplanell.validate_plane_insignia(action):
                print("Input is invalid!")
                action = input("Enter the plane insignia: ").upper()
                if action == "B":
                    self.airplane_menu()
                elif action == "Q":
                    return 'q'
            new_plane += action + ","
            delete_line(100)

            action = input("Enter the model: ").upper()
            if action == "B":
                self.airplane_menu()
            elif action == "Q":
                return 'q'
            delete_line(100)

            while not self.airplanell.validate_model(action):
                print("Input is invalid!")
                action = input("Enter the model: ").upper()
                if action == "B":
                    self.airplane_menu()
                elif action == "Q":
                    return 'q'
            new_plane += action
            delete_line(100)

            self.airplanell.create_plane(new_plane)
            action = input("Do you want to create another airplane? (y)es or (n)o: " ).lower()
            if action == "n":
                return "q"
            delete_line(100)

    def show_pilots_by_airplane_type(self):
        ''' Presents the user with every pilot with the selected flight license '''
        airio = self.airplanell.load_from_file()
        print(airio)
        type_id = input("By what plane type do you want to search? ")
        if type_id == "b":
            return
        if type_id == "q":
            return "q"
        delete_line(100)
        employio = self.airplanell.display_by_licence(type_id)
        print(employio)
        print()
        action = input('Enter "b" to go back and "q" to got to the main menu: ')
        if action == "q":
            return "q"
        delete_line(100)
    
    def show(self):
        ''' Presents the user with every plane within the system '''
        airio = self.airplanell.load_from_file()
        print(airio)
        print()
        action = input('Enter "b" to go back and "q" to got to the main menu: ')
        if action == "q":
            return "q"
        delete_line(100)

