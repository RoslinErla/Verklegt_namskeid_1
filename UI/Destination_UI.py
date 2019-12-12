from logic.Destination_LL import DestinationLL
from IO.destinationIO import DestinationIO

class DestinationUI:

    def __init__(self):
        self.__ll_destination = DestinationLL()
        self.__io_destination = DestinationIO()
    

    def add_destination(self):   
        """The user has chosen to create a new destination"""
        print("Destinations within the systems: ")
        self.__io_destination.load_destination_from_file()
        print(self.__io_destination)
        print('Enter "b" to go back and "q" to got to the main menu.')
        action = ""                                       # User puts in the name of the country
        destination = ""
        while True:
            action = input("Enter destination number: ").upper()
            if action == 'b':                                           
                break                                                   # en svo kemur "please enter your command" og þá virkar q rétt
            if action == 'q':
                return "q"
            while not self.__ll_destination.validate_destination_num(action):
                action = input("Enter destination number: ").upper()
                if action == 'b':                                           
                    break                                                   # en svo kemur "please enter your command" og þá virkar q rétt
                if action == 'q':
                    return "q"
            if action == 'b':                                           
                break  
            action = input("Enter country name: ").upper()                      # Þarf að laga: q virkar bara eins og b hér
            if action == 'b':                                           
                break                                                   # en svo kemur "please enter your command" og þá virkar q rétt
            if action == 'q':
                return "q"
            while not self.__ll_destination.validate_country_name(action):
                print("Input is invalid")
                action = input("Enter country name: ").upper()
                if action == 'b':
                    break
                if action == 'q':
                    return "q"
            if action == 'b':                                           
                break     
            destination += action
            if action == 'b':                # b virkar rétt!  
                break
            destination += action
                                                    
            action = input("Enter airport: ").upper()    # User puts in the name of the airport
            if action == 'b':
                break
            if action == 'q':
                return "q" 
            while not self.__ll_destination.validate_airport_name(action):    # velja flugvöll ?
                print("Input is invalid") 
                action = input("Enter airport: ").upper()
                if action == 'b':
                    return
                if action == 'q':
                    return "q"
            if action == 'b':
                break
            destination += action
                    # Eftir að gera validate-ið fyrir flugtíma
                                                         
            action = input("Enter flight-time: ").upper()          # User puts in the flight time
            if action == 'b':
                break
            if action == 'q':
                return "q"                                      
            while not self.__ll_destination.validate_flight_time(action):
               print("Input is invalid")
               action = input("Enter flight-time: ").upper()
               if action == 'b':
                   break
               if action == 'q':
                   return "q"
            destination += action
            if action == 'b':
               break
                                         # User puts in the distance from Iceland
            
            action = input("Enter distance from Iceland: ").upper()
            if action == 'b':
                break
            if action == 'q':
                return "q" 
            while not self.__ll_destination.validate_distance(action):
                print("Input is invalid")
                action = input("Enter distance from Iceland: ").upper()
                if action == 'b':
                    break
                if action == 'q':
                    return "q"
            if action == 'b':
                break
            destination += action
             
            action = input("Enter name of emergency contact: ").upper()
            if action == 'b':
                break
            if action == 'q':
                return "q" 
            while not self.__ll_destination.validate_contact_name(action):  
                print("Input is invalid")
                action = input("Enter name of emergency contact: ").upper()
                if action == 'b':
                    break        
                if action == 'q':
                    return "q" 
            if action == 'b':
                break  
            destination += action 

                      # User puts in the phone number of the emergency contact
            action = input("Enter emergency contact's phone number: ").upper()  
            if action == 'b':
                break
            if action == 'q':
                return "q"  
            while not self.__ll_destination.validate_contact_number(action):
                print("Invalid input").upper()
                action = input("Enter emergency contact's phone number: ").upper()
                if action == 'b':
                    break        
                if action == 'q':
                    return "q"
            if action == "b":
                break 
            destination += action

            
            action = input("Do you want to enter another destination? (y/n): ").lower()
            if action == "y":  # virkar
                continue
            if action == "n":  # virkar ekki!
                return "q"
                  
        
    def change_contact(self):
        """The user has chosen to change the name and/or phone number of the emergency contact"""
        action = ""
        contact = ""
        print('Enter "b" to go back and "q" to got to the main menu.')    # q virkar bara eins og b
        while True:
            action = input("Enter the contact's location: ").upper()           # The user inputs the location of the emergency contact
            if action == 'b':
                break
            if action == 'q':
                return "q" 
            while not self.__ll_destination.validate_destination_name(action):
                print("Invalid input").upper()
                action = input("Enter the contact's location: ").upper()
                if action == 'b':
                    break        
                if action == 'q':
                    return "q" 
            contact += action
            if action == 'b':                             # b virkar rétt!
                break
        
        # Velja númer staðsetningar innan kerfisins ? 

    def display_destination(self):
        print()
        self.__io_destination.load_destination_from_file()
        print(self.__io_destination)
        print()
            