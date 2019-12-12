from logic.Destination_LL import DestinationLL
from IO.destinationIO import DestinationIO

class DestinationUI:

    def __init__(self):
        self.__ll_destination = DestinationLL()
        self.__io_destination = DestinationIO()
    

    def add_destination(self):   
        """The user has chosen to create a new destination"""
        print('Enter "b" to go back and "q" to got to the main menu.')
        action = ""                                       # User puts in the name of the country
        destination = ""
        while True:
            
            action = input("Enter country name: ")                      # Þarf að laga: q virkar bara eins og b hér
            if action == 'b':                                           # eða þegar maður setur q inn  í Enter country name
                break                                                   # en svo kemur "please enter your command" og þá virkar q rétt
            if action == 'q':
                return "q"
            while not self.__ll_destination.validate_country_name:
                print("Input is invalid")
                action = input("Enter country name: ")
                if action == 'b':
                    break
                if action == 'q':
                    return "q"
            destination += action
            if action == 'b':                # b virkar rétt!  
                break
            destination += action
            # action = input("Enter flight number: ")     # flugnúmer á ekki að vera í destination
            # if action == 'b':
            #     break
            # if action == 'q':
            #     return "q"   
            # while not self.__ll_destination.validate_flight_number(action):
            #     print("Input is invalid")
            #     action = input("Enter flight number: ")
            #     if action == 'b':
            #         break
            #     if action == 'q':
            #         return "q"
            # destination += action
            # if action == 'b':
            #     break
                                                    
            action = input("Enter airport: ")    # User puts in the name of the airport
            if action == 'b':
                break
            if action == 'q':
                return "q" 
            while not self.__ll_destination.validate_airport_name(action):    # velja flugvöll ?
                print("Input is invalid") 
                action = input("Enter airport: ")
                if action == 'b':
                    break
                if action == 'q':
                    return "q"
            destination += action
            if action == 'b':
                break
                    # Eftir að gera validate-ið fyrir flugtíma
                                                         
            #action = input("Enter flight-time: ")          # User puts in the flight time
            # if action == 'b':
                #break
            #if action == 'q':
                #return "q"                                      
            #while not self.__ll_destination.validate_flight_time(action):
                #print("Input is invalid")
                #action = input("Enter flight-time: ")
                # if action == 'b':
                # break
                # if action == 'q':
                #     return "q"
            #destination += action
            #if action == 'b':
                #break
                                          # User puts in the distance from Iceland
            
            action = input("Enter distance from Iceland: ")
            if action == 'b':
                break
            if action == 'q':
                return "q" 
            while not self.__ll_destination.validate_distance(action):
                print("Input is invalid")
                action = input("Enter distance from Iceland: ")
                if action == 'b':
                    break
                if action == 'q':
                    return "q"
            destination += action
            if action == 'b':
                break
                                                 # User puts in the name of the emergency contact
             
            action = input("Enter name of emergency contact: ")
            if action == 'b':
                break
            if action == 'q':
                return "q" 
            while not self.__ll_destination.validate_contact_name(action):
                print("Input is invalid")
                action = input("Enter name of emergency contact: ")
            destination += action 
            if action == 'b':
                break
            if action == 'q':
                return "q"
                
                      # User puts in the phone number of the emergency contact
            
            action = input("Enter emergency contact's phone number: ")  
            if action == 'b':
                break
            if action == 'q':
                return "q"  
            while not self.__ll_destination.validate_contact_number(action):
                print("Invalid input")
                action = input("Enter emergency contact's phone number: ")
            destination += action
            if action == 'b':
                break
            if action == 'q':
                return "q"
            
            action = input("Do you want to input another destination? (y/n): ").lower
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
            action = input("Enter the contact's location: ")           # The user inputs the location of the emergency contact
            if action == 'b':
                break
            if action == 'q':
                return "q" 
            while not self.__ll_destination.validate_destination_name(action):
                print("Invalid input")
                action = input("Enter the contact's location: ")
            contact += action
            if action == 'b':                             # b virkar rétt!
                break
            if action == 'q':
                return "q"
        
        
        # Velja númer staðsetningar innan kerfisins ? 
                 

