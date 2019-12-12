from IO.airplaneIO import AirplaneIO
from logic.Airplane_LL import AirplaneLL
from IO.employeeIO import EmployeeIO


class AirplaneUI:
    def __init__(self):
        self.airplanell = AirplaneLL()
        self.airplaneio = AirplaneIO()
        self.employeeio = EmployeeIO()
    def airplane_menu(self):
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

    def call_on_validate_and_create(self):
        print('Enter "b" to go back and "q" to got to the main menu.')
        action = ""
        new_plane = ""
        while True:
            action = input("Enter the manufacturer: ").upper()
            if action == "B":
                self.airplane_menu()
            elif action == "Q":
                return 'q'

            while not self.airplanell.validate_manufacturer(action):
                print("Input is invalid!")
                action = input("Enter the manufacturer: ").upper()
                if action == "B":
                    self.airplane_menu()
                elif action == "Q":
                    return 'q'          
            new_plane += action + ","


            action = input("Enter the type ID: ").upper()
            if action == "B":
                self.airplane_menu()
            elif action == "Q":
                return 'q'

            while not self.airplanell.validate_typeID(action):
                print("Input is invalid!")
                action = input("Enter the type ID: ").upper()
                if action == "B":
                    self.airplane_menu()
                elif action == "Q":
                    return 'q'
            new_plane += action + ","

            action = input("Enter the plane insignia: ").upper()
            if action == "B":
                    self.airplane_menu()
            elif action == "Q":
                return 'q'

            while not self.airplanell.validate_plane_insignia(action):
                print("Input is invalid!")
                action = input("Enter the plane insignia: ").upper()
                if action == "B":
                    self.airplane_menu()
                elif action == "Q":
                    return 'q'
            new_plane += action + ","

            action = input("Enter the model: ").upper()
            if action == "B":
                self.airplane_menu()
            elif action == "Q":
                return 'q'

            while not self.airplanell.validate_model(action):
                print("Input is invalid!")
                action = input("Enter the model: ").upper()
                if action == "B":
                    self.airplane_menu()
                elif action == "Q":
                    return 'q'
            new_plane += action

            self.airplanell.create_plane(new_plane)
            action = input("Do you want to create another airplane? (y)es or (n)o: " ).lower()
            if action == "n":
                return "q"

    def show_pilots_by_airplane_type(self):
        self.airplaneio.load_airplane_from_file()
        print(self.airplaneio)
        type_id = input("By what plane type do you want to search? ")
        if type_id == "b":
            return
        if type_id == "q":
            return "q"
        self.employeeio.display_by_licence(type_id)
        print(self.employeeio)



    # def call_on_validate_and_change(self):
    #     while True:
    #         self.airplaneio.load_airplane_from_file()
    #         print(self.airplaneio)
    #         print()
    #         planeinsignia = input("Please enter the Plane Insignia of the employee who's information you want to edit: ")
    #         if planeinsignia == "q":
    #             return "q"
    #         if planeinsignia == "b":
    #             break
    #         change = input("Please enter what you wish to change: ")
    #         if change == "q":
    #             return "q"
    #         if change == "b":
    #             break
    #         new = input("Please enter the new entry for {}".format(change))
    #         if new == "q":
    #             return "q"
    #         if new == "b":
    #             break
    #         print()
    #         self.airplanell.change_plane(planeinsignia, change, new)
    #         action = input("Do you want to change another airplane? (y)es or (n)o: " ).lower()
    #         if action == "n":
    #             action = "q"
        
    
    def show(self):
        print()
        self.airplaneio.load_airplane_from_file()
        print(self.airplaneio)
        print()

    # def print_status(self,a_list):
    #     return "{:12} | {:15} | {:15} | {:6}".format(self.__manufacturer, self.__type_ID, self.__plane_insignia, self.__model)
        

    # def status(self):
    #     a.print_status()


    # flight_number = [NA,X,X,X]
    # joined = flight_number.join()
