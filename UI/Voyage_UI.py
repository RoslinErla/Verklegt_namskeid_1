from logic.Voyage_LL import VoyageLL
from model.VoyageM import Voyage
from logic.Destination_LL import DestinationLL
# from UI.Main_UI import MainUI ?



class VoyageUI:

    def __init__(self):
        self.__ll_voyage = VoyageLL()
        self.__ll_destination = DestinationLL()
        #self.__ui_main = MainUI

    def create_voyage(self):  
        pass

    def voyage_menu(self): 
        """ The user can choose between the create, change and display options in the system"""
        action = ""
        if (action != "q" or "b"):
            print("The following actions are possible: ")
            print("\tEnter 1 to create a voyage within the system.")
            print("\tEnter 2 to change voyages already within the system.")
            print("\tEnter 3 to display voyages within the system.")
            print("Enter b or q to got to the main menu.")
           
            action = input("Please enter your command: ").lower()

        if action == "1":
            self.create_menu()
            
        if action == "2":
            self.change_menu()
            
        if action == "3":
            self.display_menu()
               
    
    def create_menu(self):
        """After the user has chosen the "create" option, he has three new options"""
        action = ""
        if (action != "q" or "b"):
            print("\tEnter 1 to repeat an old voyage")
            print("\tEnter 2 to create a new voyage")
            print("\tEnter 3 to create a new destination")

            action = input("Please enter your commmand: ").lower()
        
        if action == "1":
            self.repeat_voyage()
        
        if action == "2":
            self.new_voyage()
        
        if action =="3":
            self.new_destination()

        if action == 'b':
            self.voyage_menu() 
            
        """if action == 'q':
            self.__ui_main.main_menu()   #Hvernig kallar maður á main_menu fallið úr Main_UI ??"""
              
        
    def change_menu(self):
        """After the user has chosen the "change" option, he has two new options"""
        action = ""
        if (action != "q" or "b"):
            print("\tEnter 1 to change voyage state")
            print("\tEnter 2 to change emergency contact's name and/or phone number")

            action = input("Please enter your commmand: ").lower()
        
        if action == "1":
            self.change_voyage_state()
        
        if action == "2":
            self.change_emergency_contact()
        
        if action == 'b':
            self.voyage_menu() 
        
            
    def display_menu(self):
        """After the user has chosen the "display" option, he has three new options"""
        action = ""
        if (action != "q" or "b"):
            print("\tEnter 1 for a daily list of voyages")
            print("\tEnter 2 for a list of flight numbers")
            print("\tEnter 3 to see the state of the voyages for today")
            action = input("Please enter your commmand: ").lower()
        
        if action == "1":
            self.daily_list()
        
        if action == "2":
            self.flight_numbers()
        
        if action == "3":
            self.daily_voyage_state()
        
        if action == 'b':
            self.voyage_menu() 
        

    def repeat_voyage(self):
        """The user has chosen to repeat an old voyage"""
        action = ""
        if (action != "q" or "b"):
            input("Enter destination: ").lower()      # Vantar virkni hér inn sem leyfir notandanum að endurtaka ferð
    
    def new_voyage(self):
        """The user has chosen to create a new voyage"""
        action = ""
        new_voyage = ""
        if action != "b" or action != "q":
            action =  input("Enter the captain's SSN: ")
            while not self.__ll_voyage.validate_captain(action):
                print("Input is invalid")
                action = input("Enter the captain's SSN: ")
            new_voyage += action
        
        if action != "b" or action != "q":
            action = input("Enter the co-pilot's SSN: ")
            while not self.__ll_voyage.validate_co_pilot(action):
                print("Input is invalid")
                action = input("Enter the co-pilot's SSN: ")
            new_voyage += action
        
        if action != "b" or action != "q":
            action = input("Enter the flight service manager's SSN: ")
            while not self.__ll_voyage.validate_fsm(action):
                print("Input is invalid")
                action = input("Enter the flight service manager's SSN: ")
            new_voyage += action
        
        if action != "b" or action != "q":
            action = input("Enter the first flight servant's SSN: ")
            while not self.__ll_voyage.validate_fa1(action):
                print("Input is invalid")
                action = input("Enter the first flight servant's SSN: ")
            new_voyage += action
        
        if action != "b" or action != "q":
            action = input("Enter the second flight servant's SSN: ")
            while not self.__ll_voyage.validate_fa2(action):
                print("Input is invalid")
                action = input("Enter the second flight servant's SSN: ")
            new_voyage += action
                
    
    def new_destination(self):   # Vantar mögulega Land (country)
        """The user has chosen to create a new destination"""
        action = ""
        destination = ""
        if action != "b" or action != "q": 
            action = input("Enter flight number: ")    # Ekki viss hvort flight number eigi að vera hér
            while not self.__ll_voyage.validate_flight_number(action):
                print("Input is invalid")
                action = input("Enter flight number: ")
            destination += action
    
        if action  != "b" or action != "q":
            action = input("Enter airport: ")
            while not self.__ll_destination.validate_airport_name(action):
                print("Input is invalid") 
                action = input("Enter airport: ")
            destination += action    

        #if action  != "b" or action != "q":                 # Eftir að gera validate-ið fyrir flugtíma
            action = input("Enter flight-time: ")
            #while not self.__ll_destination.validate_flight_time(action):
                #print("Input is invalid")
                #action = input("Enter flight-time: ")
            #destination += action    
        
        if action  != "b" or action != "q": 
            action = input("Enter distance from Iceland: ")
            while not self.__ll_destination.validate_distance(action):
                print("Input is invalid")
                action = input("Enter distance from Iceland: ")
            destination += action   
        
        if action  != "b" or action != "q": 
            action = input("Enter name of emergency contact: ")
            while not self.__ll_destination.validate_contact_name(action):
                print("Input is invalid")
                action = input("Enter name of emergency contact: ")
            destination += action 
        
        if action  != "b" or action != "q":
            action = input("Enter emergency contact's phone number: ")    
            while not self.__ll_destination.validate_contact_number(action):
                print("Invalid input")
                action = input("Enter emergency contact's phone number: ")
            destination += action 
                
    
    def change_voyage_state(self):
        """The user has chosen to change the state of the voyage"""
        input("Enter destination: ")   
        input("Enter date and time: ")
        # Breyta stöðunni!
    

    def change_emergency_contact(self):
        """The user has chosen to change the name and/or phone number of the emergency contact"""
        #Veljið stað tengiliðs?
        #Númer staðsetningar innan kerfisins ? 
        pass

    def daily_list(self):
        """The user has chosen to have a list of voyages for a given day displayed"""
        input("Enter a date: ")
        # Birta listannn ! 
    
    def flight_numbers(self):
        """The user has chosen to have a list of flight numbers for a given date displayed"""
        input("Enter destination: ")
        input("Enter a date: ")
        # Birta lista flugnúmera fyrir innslegna dagsetningu
    
    def daily_voyage_state(self):
        """The user has chosen to have a list of voyage's state (finished, arrived or cancelled) displayed """
        input("Enter a date: ")
        # Birta lista vinnuferða þar sem sést hvaða ferðum er lokið, lent ytra og eða felld niður




    






        

        

            



 
      

        
