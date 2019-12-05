"""from logic.Voyage_LL import VoyageLL
from model.VoyageM import Voyage"""



class VoyageUi:

    def __init__(self):
        self.__ll_voyage = VoyageLL()

    def create_flight(self):   # Bæta við ferð ... ?
        pass


    def voyage_menu(self): 
        action = ""
        while(action != "q" or "b"):
            print("The following actions are possible: ")
            print("\tEnter 1 to create a voyage within the system.")
            print("\tEnter 2 to change voyages already within the system.")
            print("\tEnter 3 to display voyages within the system.")
            print("Enter b to go back and q to got to the main menu.")
           

            action = input("Please enter your command: ").lower()

            if action == 1:
                create_voyage = create_menu()
            
            if action == 2:
                change_voyage = change_menu()
            
            if action == 3:
                display_voyage = display_menu()


    
    def create_menu(self):
        action_create = ""
        while(action != "q" or "b"):
            print("\tEnter 1 to repeat an old voyage")
            print("\tEnter 2 to create a new voyage")
            print("\tEnter 3 to create a new destination")

            action_create = input("Please enter your commmand: ")
        
        return action_create

        
    
    def change_menu(self):
        action_change = ""
        while(action != "q" or "b"):
            print("\tEnter 1 to change voyage state")
            print("\tEnter 2 to change emergency contact's name and/or phone number")

            action_change = input("Please enter your commmand: ")
        
        return action_change


    def display_menu(self):
        action_display = ""
        while(action != "q" or "b"):
            print("\tEnter 1 for a daily list of voyages")
            print("\tEnter 2 for a weakly list of voyages")
            print("\tEnter 3 for a list of flight numbers")
            print("\tEnter 4 to see the state of the voyages for today")
            action_display = input("Please enter your commmand: ")
        
        return action_display



            

        
