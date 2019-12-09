from logic.Voyage_LL import VoyageLL
from model.VoyageM import Voyage
from logic.Destination_LL import DestinationLL
from IO.destinationIO import DestinationIO



class VoyageUI:

    def __init__(self):
        self.__ll_voyage = VoyageLL()
        self.__ll_destination = DestinationLL()
        self.__io_destination = DestinationIO()

    def create_voyage(self):  
        pass

    def change_voyage(self):
        pass


    def voyage_menu(self): 
        """ The user can choose between the create, change and display options in the system"""
        action = ""
        leave = ''
        while action != "b" and leave != "q":
            print("The following actions are possible: ")
            print("\tEnter 1 to create a voyage within the system.")
            print("\tEnter 2 to change voyages already within the system.")
            print("\tEnter 3 to display voyages within the system.")
            print("Enter b or q to got to the main menu.")
           
            action = input("Please enter your command: ").lower()

            if action == "1":
                leave = self.create_menu()
            
            if action == "2":
                leave = self.change_menu()
            
            if action == "3":
                leave = self.display_menu()
        
            if action == "b" or action == "q":
                break              
    
    def create_menu(self):
        """After the user has chosen the "create" option, he has three new options"""
        action = ""
        leave = ''
        while action != "b" and leave != "q":
            print("\tEnter 1 to repeat an old voyage")
            print("\tEnter 2 to create a new voyage")
            print("\tEnter 3 to create a new destination")
            print('Enter "b" to go back and "q" to got to the main menu.')

            action = input("Please enter your commmand: ").lower()
        
            if action == "1":
                self.repeat_voyage()
        
            if action == "2":
                self.new_voyage()
        
            if action =="3":
                self.new_destination()

            if action == 'b':
                self.voyage_menu() 
            
            if action == 'q':
                return "q"
              
        
    def change_menu(self):
        """After the user has chosen the "change" option, he has two new options"""
        action = ""
        while (action != "q" or "b"):
            print("\tEnter 1 to change voyage state")
            print("\tEnter 2 to change emergency contact's name and/or phone number")
            print('Enter "b" to go back and "q" to got to the main menu.')

            action = input("Please enter your commmand: ").lower()
        
            if action == "1":
                self.change_voyage_state()
        
            if action == "2":
                self.change_emergency_contact()
        
            if action == 'b':
                self.voyage_menu() 
        
            if action == 'q':
                return "q"
        
            
    def display_menu(self):
        """After the user has chosen the "display" option, he has three new options"""
        action = ""
        while (action != "q" or "b"):
            print("\tEnter 1 for a daily list of voyages")
            print("\tEnter 2 for a list of flight numbers")
            print("\tEnter 3 to see the state of the voyages for today")
            print('Enter "b" to go back and "q" to got to the main menu.')
            action = input("Please enter your commmand: ").lower()
        
            if action == "1":
                self.daily_list()
        
            if action == "2":
                self.flight_numbers()
        
            if action == "3":
                self.daily_voyage_state()
        
            if action == 'b':
                self.voyage_menu() 
        
            if action == 'q':
                return "q"
        

    def repeat_voyage(self):
        """The user has chosen to repeat an old voyage"""
        action = ""
        
        print('Enter "b" to go back and "q" to got to the main menu.')
        action = input("Enter destination: ").lower()      # Vantar virkni hér inn sem leyfir notandanum að endurtaka ferð
        
        if action == 'b':
            self.create_menu()
        
        if action == 'q':
            return "q" 
    
    def new_voyage(self):
        """The user has chosen to create a new voyage"""
        action = ""
        new_voyage = ""
        print('Enter "b" to go back and "q" to got to the main menu.')
        if action != "b" or action != "q":
            action =  input("Enter the captain's SSN: ")
            while not self.__ll_voyage.validate_SSN(action):
                print("Input is invalid")
                action = input("Enter the captain's SSN: ")
            new_voyage += action
        
        
        if action != "b" or action != "q":
            action = input("Enter the co-pilot's SSN: ")
            while not self.__ll_voyage.validate_SSN(action):
                print("Input is invalid")
                action = input("Enter the co-pilot's SSN: ")
            new_voyage += action
        
        if action != "b" or action != "q":
            action = input("Enter the flight service manager's SSN: ")
            while not self.__ll_voyage.validate_SSN(action):
                print("Input is invalid")
                action = input("Enter the flight service manager's SSN: ")
            new_voyage += action
        
        if action != "b" or action != "q":
            action = input("Enter the first flight servant's SSN: ")
            while not self.__ll_voyage.validate_SSN(action):
                print("Input is invalid")
                action = input("Enter the first flight servant's SSN: ")
            new_voyage += action
        
        if action != "b" or action != "q":
            action = input("Enter the second flight servant's SSN: ")
            while not self.__ll_voyage.validate_SSN(action):
                print("Input is invalid")
                action = input("Enter the second flight servant's SSN: ")
            new_voyage += action
        
        if action == 'b':
            self.create_menu()

        if action == 'q':
            return "q"
                
    
    def new_destination(self):   # Vantar mögulega Land (country)
        """The user has chosen to create a new destination"""
        action = ""
        destination = ""
        print('Enter "b" to go back and "q" to got to the main menu.')
        if action != "b" or action != "q": 
            action = input("Enter flight number: ")    # Ekki viss hvort flight number eigi að vera hér
            while not self.__ll_voyage.validate_flight_number(action):
                print("Input is invalid")
                action = input("Enter flight number: ")
            destination += action
    
        if action  != "b" or action != "q":
            action = input("Enter airport: ")                                     # velja flugvöll ?
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
        
        if action == 'b':
            self.create_menu()
        
        if action == 'q':
            return "q"
                
    
    def change_voyage_state(self):
        """The user has chosen to change the state of the voyage"""
        action = ""
        print('Enter "b" to go back and "q" to got to the main menu.')
        self.__io_destination.load_destination_from_file()                   # Hægt að velja destination frá lista
        input("Enter destination id: ")                                      
        input("Enter date and time: ")
        # Breyta stöðunni!

        if action == 'b':
            self.change_menu()
        
        if action == 'q':
            return "q"
    

    def change_emergency_contact(self):
        """The user has chosen to change the name and/or phone number of the emergency contact"""
        action = ""
        print('Enter "b" to go back and "q" to got to the main menu.')
        #Veljið stað tengiliðs?
        #Númer staðsetningar innan kerfisins ? 
        if action == 'b':
            self.change_menu()
        
        if action == 'q':
            return "q"

    def daily_list(self):
        """The user has chosen to have a list of voyages for a given day displayed"""
        action = ""
        print('Enter "b" to go back and "q" to got to the main menu.')
        input("Enter a date: ")
        # Birta listannn ! 
        if action == 'b':
            self.display_menu()
        
        if action == 'q':
            return "q"
    
    def flight_numbers(self):
        """The user has chosen to have a list of flight numbers for a given date displayed"""
        action = ""
        print('Enter "b" to go back and "q" to got to the main menu.')
        input("Enter destination: ")
        input("Enter a date: ")
        # Birta lista flugnúmera fyrir innslegna dagsetningu
        if action == 'b':
            self.display_menu()
        
        if action == 'q':
            return "q"
    
    def daily_voyage_state(self):
        """The user has chosen to have a list of voyage's state (finished, arrived or cancelled) displayed """
        action = ""
        print('Enter "b" to go back and "q" to got to the main menu.')
        input("Enter a date: ")
        # Birta lista vinnuferða þar sem sést hvaða ferðum er lokið, lent ytra og eða felld niður
        if action == 'b':
            self.display_menu()
        
        if action == 'q':
            return "q"




    






        

        

            



 
      

        
