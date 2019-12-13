from logic.Destination_LL import DestinationLL
from IO.destinationIO import DestinationIO

import string

class DestinationUI:

    def __init__(self):
        self.__ll_destination = DestinationLL()
        self.__io_destination = DestinationIO()
    
    def destination_menu(self):
        ''' Presents the user with  '''
        leave = ""
        while leave != "q":    
            print("\tDestination Menu")
            print()
            print("The following actions are possible:")
            print('\t1. Enter "1" to create a new destination within the system.')
            print('\t2. Enter "2" to change a destinations emergency contact.')
            print('\t3. Enter "3" to display destinations within the system.')
            print()
            action = input("Please enter your command: ")
            action = action.lower()
    
            if action == "1":
                leave = self.add_destination()
            elif action == "2":
                leave =  self.change_contact()
            elif action == "3":
                leave == self.display_destination()
            elif action == "b" or action == "q":
                break
            
    def add_destination(self):   
        """The user has chosen to create a new destination"""
        print("Destinations within the systems: ")
        self.__io_destination.load_destination_from_file()
        print(self.__io_destination)
        print('Enter "b" to go back and "q" to got to the main menu.')
        action = ""                                       # User puts in the name of the country
        destination = ""
        while True:
            action = input("Enter destination number: ")
            if action == 'b':                                           
                break                                                   # en svo kemur "please enter your command" og þá virkar q rétt
            if action == 'q':
                return "q"
            while self.__ll_destination.check_if_exists(action,0):
                print("Input is invalid!")
                action = input("Enter destination number: ").upper()
                if action == 'b':                                           
                    break                                                   # en svo kemur "please enter your command" og þá virkar q rétt
                if action == 'q':
                    return "q"

            destination += action + ","

            self.__io_destination.load_destination_from_file()
            print(self.__io_destination)
            action = input("Enter the destination name: ")
            print()
            if action == 'b':
                self.destination_menu()
            if action == 'q':
                return "q"

            while not self.__ll_destination.validate_destination_name(action):
                print("Input is invalid!")
                self.__io_destination.load_destination_from_file()
                print(self.__io_destination)
                action = input("Enter the destination name: ")
                print()
                if action.lower() == 'b':
                    self.destination_menu()
                if action.lower() == 'q':
                    return "q"

            action = input("Enter destination id")

            if action == 'b':
                self.destination_menu()
            if action == 'q':
                return "q"
            
            while not self.__ll_destination.validate_destination_id(action):
                print("Input is invalid")
                action = input("Enter destination id")
                if action.lower() == "b":
                    self.destination_menu()
                if action.lower() == "q":
                    return "q"

            destination += action + ","

            action = input("Enter country name: ")                      # Þarf að laga: q virkar bara eins og b hér
            if action.lower() == 'b':                                           
                break                                                   # en svo kemur "please enter your command" og þá virkar q rétt
            if action.lower() == 'q':
                return "q"

            while not self.__ll_destination.validate_country_name(action):
                print("Input is invalid!")
                action = input("Enter country name: ")
                if action.lower() == 'b':
                    break
                if action.lower() == 'q':
                    return "q"

            destination += action + ","
                                                    
            action = input("Enter airport: ")    # User puts in the name of the airport
            if action.lower() == 'b':
                break
            if action.lower() == 'q':
                return "q" 
            while not self.__ll_destination.validate_airport_name(action):    # velja flugvöll ?
                print("Input is invalid!") 
                action = input("Enter airport: ").upper()
                if action == 'b':
                    return
                if action == 'q':
                    return "q"
            if action == 'b':
                break
            destination += action + ","
                                                         
            action = input("Enter flight-time: ")          # User puts in the flight time
            if action == 'b':
                break
            if action == 'q':
                return "q"                                      
            while not self.__ll_destination.validate_flight_time(action):
               print("Input is invalid!")
               action = input("Enter flight-time(hours.minutes): ")
               if action == 'b':
                   break
               if action == 'q':
                   return "q"

            destination += action + ","
            
            action = input("Enter distance from Iceland: ")
            if action.lower() == 'b':
                break
            if action.lower() == 'q':
                return "q" 

            while not self.__ll_destination.validate_distance(action):
                print("Input is invalid!")
                action = input("Enter distance from Iceland in km: ")
                if action.lower() == 'b':
                    break
                if action.lower() == 'q':
                    return "q"

            destination += action + "km" +","
             
            action = input("Enter name of emergency contact: ")

            if action.lower() == 'b':
                break
            if action.lower() == 'q':
                return "q" 

            while not self.__ll_destination.validate_contact_name(action):  
                print("Input is invalid!")
                action = input("Enter name of emergency contact: ")
                if action.lower() == 'b':
                    break        
                if action.lower() == 'q':
                    return "q" 
 
            destination += action + ","

                      # User puts in the phone number of the emergency contact
            action = input("Enter emergency contact's phone number: ") 
            if action.lower() == 'b':
                break
            if action.lower() == 'q':
                return "q"  
            while not self.__ll_destination.validate_contact_number(action):
                print("Invalid input")
                action = input("Enter emergency contact's phone number: ")
                if action.lower() == 'b':
                    break        
                if action.lower() == 'q':
                    return "q"
            destination += action

            
            action = input("Do you want to enter another destination? (y/n): ").lower()
            if action == "y":  # virkar
                continue
            if action == "n":  # virkar ekki!
                return "q"

        
    def change_contact(self):
        """ The user has chosen to change the name and/or phone number of the emergency contact"""
        action = ""
        contact = ""
        print('Enter "b" to go back and "q" to got to the main menu.')    # q virkar bara eins og b
        while True:
            print()
            self.__io_destination.load_destination_from_file()
            print(self.__io_destination)
            action = input("Enter the contact's destination ID: ").upper()           # The user inputs the location of the emergency contact
            if action.lower() == 'b':
                break
            if action.lower() == 'q':
                return "q" 
            while self.__ll_destination.check_if_exists(action,2):
                print("Invalid input")
                self.__io_destination.load_destination_from_file()
                print(self.__io_destination)
                action = input("Enter the contact's destination ID: ").upper()
            contact = action
            if action == 'b':
                break        
            elif action == 'q':
                return "q" 
        
            print("Enter 1 to change the name of the emergency contact")
            print("Enter 2 to change the emergency contact's phone number")
            action = input("Please enter you command: ")

            if action == "1":
                change = "emergency contact"
                new = input("Please enter the new entry for {}: ".format(change))
                while not self.__ll_destination.validate_contact_name(new):
                    print("Input is invalid!")
                    new = input("Please enter the new entry for {}:".format(change))
            
            elif action == "2":
                change = "emergency phone"
                new = input("Please enter the new entry for {}: ".format(change))
                while not self.__ll_destination.validate_contact_number(new):
                    print("Input is invalid!")
                    new = input("Please enter the new entry for {}: ".format(change))

            elif action == 'b':
                break        
            elif action == 'q':
                return "q" 

            self.__io_destination.change_destination(contact,change,new)

            action = input("Do you want to change another employee? (y)es or (n)o: " ).lower()
            if action == "n":
                return "q"

    def display_destination(self):
        ''' Calls for "load_destination_from_file" from "Destination_UI.py" to display every destination within the system. '''
        print()
        self.__io_destination.load_destination_from_file()
        print(self.__io_destination)
        input("Press 'q' to go back: ")
        print()
            
