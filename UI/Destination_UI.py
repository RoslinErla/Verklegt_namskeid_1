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
            action = input("Enter country name: ")    
            while not self.__ll_destination.validate_country_name:
                print("Input is invalid")
                action = input("Enter country name: ")
            destination += action
            if action == 'b':
                break
            if action == 'q':
                return "q"
            action = input("Enter flight number: ")    
            while not self.__ll_destination.validate_flight_number(action):
                print("Input is invalid")
                action = input("Enter flight number: ")
            destination += action
            if action == 'b':
                break
            if action == 'q':
                return "q"

                                                    
            action = input("Enter airport: ")    # User puts in the name of the airport
            while not self.__ll_destination.validate_airport_name(action):    # velja flugvöll ?
                print("Input is invalid") 
                action = input("Enter airport: ")
            destination += action
            if action == 'b':
                break
            if action == 'q':
                return "q"
                    # Eftir að gera validate-ið fyrir flugtíma

                                                         
            #action = input("Enter flight-time: ")          # User puts in the flight time                                        
            #while not self.__ll_destination.validate_flight_time(action):
                #print("Input is invalid")
                #action = input("Enter flight-time: ")
            #destination += action
            #if action == 'b':
                #break
            #if action == 'q':
                #return "q"
                                          # User puts in the distance from Iceland
            
            action = input("Enter distance from Iceland: ")
            while not self.__ll_destination.validate_distance(action):
                print("Input is invalid")
                action = input("Enter distance from Iceland: ")
            destination += action
            if action == 'b':
                break
            if action == 'q':
                return "q"
                                                 # User puts in the name of the emergency contact
            
           
            action = input("Enter name of emergency contact: ")
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
            while not self.__ll_destination.validate_contact_number(action):
                print("Invalid input")
                action = input("Enter emergency contact's phone number: ")
            destination += action
            if action == 'b':
                break
            if action == 'q':
                return "q"
                 

