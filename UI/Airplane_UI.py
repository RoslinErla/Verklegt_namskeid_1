from logic.Airplane_LL import AirplaneLL 
from UI.frame import Frame

class AirplaneUI:
    def __init__(self):
        self.airplanell = AirplaneLL()
        self.frame = Frame()
    
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
            print('\t4. enter "4" to display planes by their status.')
            print('Enter "b" to go back and "q" to got to the main menu.')

            action = input("Please enter your command: ")
            print()

            action = action.lower()
            self.frame.clear_all()
            

            if action == "1":
                leave = self.call_on_validate_and_create()
            if action == "2":
                leave = self.show_pilots_by_airplane_type()
            if action == "3":
                leave = self.show()
            if action == "4":
                leave = self.show_by_status()
            if action == "b" or action == "q":
                break

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
            self.frame.clear_all()
        
            while not self.airplanell.validate_manufacturer(action):
                print("Input is invalid!")
                action = input("Enter the manufacturer: ").upper()
                if action == "B":
                    self.airplane_menu()
                elif action == "Q":
                    return 'q'
            new_plane += action + ","
            self.frame.clear_all()



            action = input("Enter the type ID: ").upper()
            if action == "B":
                self.airplane_menu()
            elif action == "Q":
                return 'q'
            self.frame.clear_all()

            while not self.airplanell.validate_typeID(action):
                print("Input is invalid!")
                action = input("Enter the type ID: ").upper()
                if action == "B":
                    self.airplane_menu()
                elif action == "Q":
                    return 'q'
            new_plane += action + ","
            self.frame.clear_all()

            action = input("Enter the plane insignia: ").upper()
            if action == "B":
                self.airplane_menu()
            elif action == "Q":
                return 'q'
            self.frame.clear_all()

            while not self.airplanell.validate_plane_insignia(action):
                print("Input is invalid!")
                action = input("Enter the plane insignia: ").upper()
                if action == "B":
                    self.airplane_menu()
                elif action == "Q":
                    return 'q'
            new_plane += action + ","
            self.frame.clear_all()

            action = input("Enter the model: ").upper()
            if action == "B":
                self.airplane_menu()
            elif action == "Q":
                return 'q'
            self.frame.clear_all()

            while not self.airplanell.validate_model(action):
                print("Input is invalid!")
                action = input("Enter the model: ").upper()
                if action == "B":
                    self.airplane_menu()
                elif action == "Q":
                    return 'q'
            new_plane += action

            self.frame.clear_all()

            self.airplanell.create_plane(new_plane)
            action = input("Do you want to create another airplane? (y)es or (n)o: " ).lower()
            if action == "n":
                return "q"
            self.frame.clear_all()
    
    def show_pilots_by_airplane_type(self):
        ''' Presents the user with every pilot with the selected flight license '''
        airio = self.airplanell.load_from_file()
        print(airio)
        type_id = input("By what plane type do you want to search? ")
        if type_id == "b":
            return
        if type_id == "q":
            return "q"
        self.frame.clear_all()

        employio = self.airplanell.display_by_licence(type_id)
        print(employio)
        print()
        action = input('Enter "b" to go back and "q" to got to the main menu: ')
        if action == "q":
            return "q"
        self.frame.clear_all()
    
    def show(self):
        ''' Presents the user with every plane within the system '''
        airio = self.airplanell.load_from_file()
        print(airio)
        print()
        action = input('Enter "b" to go back and "q" to got to the main menu: ')
        if action == "q":
            return "q"
            
        self.frame.clear_all()

    def show_by_status(self):
        pass

