from logic.Voyage_LL import VoyageLL
from model.VoyageM import Voyage
from logic.Destination_LL import DestinationLL



class VoyageUI:

    def __init__(self):
        self.__ll_voyage = VoyageLL()
        self.__ll_destination = DestinationLL()

    def create_voyage(self):  
        pass

    def voyage_menu(self): 
        action = ""
        if (action != "q" or "b"):
            print("The following actions are possible: ")
            print("\tEnter 1 to create a voyage within the system.")
            print("\tEnter 2 to change voyages already within the system.")
            print("\tEnter 3 to display voyages within the system.")
            print("Enter b to go back and q to got to the main menu.")
           

            action = input("Please enter your command: ").lower()

        if action == "1":
            self.create_menu()
            
        if action == "2":
            self.change_menu()
            
        if action == "3":
            self.display_menu()
               
    
    def create_menu(self):
        action_create = ""
        if (action_create != "q" or "b"):
            print("\tEnter 1 to repeat an old voyage")
            print("\tEnter 2 to create a new voyage")
            print("\tEnter 3 to create a new destination")

            action_create = input("Please enter your commmand: ")
        
        if action_create == "1":
            self.repeat_voyage()
        
        if action_create == "2":
            self.new_voyage()
        
        if action_create =="3":
            self.new_destination()

     
        
    def change_menu(self):
        action_change = ""
        if (action_change != "q" or "b"):
            print("\tEnter 1 to change voyage state")
            print("\tEnter 2 to change emergency contact's name and/or phone number")

            action_change = input("Please enter your commmand: ")
        
        if action_change == "1":
            self.change_voyage_state()
        
        if action_change == "2":
            self.change_emergency_contact()
        
            
    def display_menu(self):
        action_display = ""
        if (action_display != "q" or "b"):
            print("\tEnter 1 for a daily list of voyages")
            print("\tEnter 2 for a list of flight numbers")
            print("\tEnter 3 to see the state of the voyages for today")
            action_display = input("Please enter your commmand: ")
        
        if action_display == "1":
            self.daily_list()
        
        if action_display == "2":
            self.flight_numbers()
        
        if action_display == "3":
            self.daily_voyage_state()
        

    def repeat_voyage(self):
        action_repeat = ""
        if (action_repeat != "q" or "b"):
            input("Enter destination: ")
    
    def new_voyage(self):
        input("Enter the name and SSN of the captain: ")
        input("Enter the name and SSN of the co-pilot: ")
        input("Enter the name and SSN of the flight service manager: ")
        input("Enter the name and SSN of the flight servant: ")

        # Setja inn starfsmenn (flugmenn og flugþjóna)

    
    def new_destination(self):   # Vantar mögulega Land (country)
        destination_action = ""
        destination = ""
        if destination_action != "b" or destination_action != "B": 
            destination_action = input("Enter flight number: ") 
            while not self.__ll_voyage.validate_flight_number(destination_action):
                print("Input is invalid")
                destination_action = input("Enter flight number: ")
            destination += destination_action
    
        if destination_action  != "b" or destination_action != "B":
            destination_action = input("Enter airport: ")
            while not self.__ll_destination.validate_airport_name(destination_action):
                print("Input is invalid") 
                destination_action = input("Enter airport: ")
            destination += destination_action    

        #if destination_action  != "b" or destination_action != "B": 
            destination_action = input("Enter flight-time: ")
            #while not self.__ll_destination.validate_flight_time(destination_action):
                #print("Input is invalid")
                #destination_action = input("Enter flight-time: ")
            #destination += destination_action    
        
        if destination_action  != "b" or destination_action != "B": 
            destination_action = input("Enter distance from Iceland: ")
            while not self.__ll_destination.validate_distance(destination_action):
                print("Input is invalid")
                destination_action = input("Enter distance from Iceland: ")
            destination += destination_action   
        
        if destination_action  != "b" or destination_action != "B": 
            destination_action = input("Enter name of emergency contact: ")
            while not self.__ll_destination.validate_contact_name(destination_action):
                print("Input is invalid")
                destination_action = input("Enter name of emergency contact: ")
            destination += destination_action 
        
        if destination_action  != "b" or destination_action != "B":
            destination_action = input("Enter emergency contact's phone number: ")    
            while not self.__ll_destination.validate_contact_number(destination_action):
                print("Invalid input")
                destination_action = input("Enter emergency contact's phone number: ")
            destination += destination_action 
                

    
    def change_voyage_state(self):
        input("Enter destination: ")
        input("Enter date and time: ")
    

    def change_emergency_contact(self):
        #Veljið stað tengiliðs?
        #Númer staðsetningar innan kerfisins ? 
        pass

    def daily_list(self):
        input("Enter a date: ")
        # Birta listannn ! 
    
    def flight_numbers(self):
        input("Enter destination: ")
        input("Enter a date: ")
        # Birta lista flugnúmera fyrir innslegna dagsetningu
    
    def daily_voyage_state(self):
        input("Enter a date: ")
        # Birta lista vinnuferða þar sem sést hvaða ferðum er lokið, lent ytra og eða felld niður




    






        

        

            



 
      

        
