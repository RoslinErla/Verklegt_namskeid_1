from logic.Voyage_LL import VoyageLL
from model.VoyageM import Voyage



class VoyageUi:

    def __init__(self):
        self.__ll_voyage = VoyageLL()

    def create_flight(self):   # Bæta við flugi ... 
        pass


    def voyage_menu(self): 
        action = ""
        while(action != "q" or "b"):
            print("The following actions are possible: ")
            print("\tEnter 1 to create a voyage within the system.")
            print("\tEnter 2 to change voyages already within the system.")
            print("\tEnter 3 to display voyages within the system.")
            print("Enter b to go back and q to got to the main menu.")
           

            action = input("Please enter your command").lower()

            if action == 1:
                old_voyage = print("\tEnter 1 to repeat an old voyage")
                new_voyage = print("\tEnter 2 to create a new voyage")
                new_destination = print("\tEnter 3 to create a new destination")
                create_
            
            if action == 2:
                change_voyage_state = print("\tEnter 1 to change voyage state)
                change_emergency_contact = print("\tEnter 2 to change emergency contact's name and/or phone number")
            
            if action == 3:
                daily_voyages_list = print("\tEnter 1 for a daily list of voyages")
                weakly_voyages_list = print("\tEnter 2 for a weakly list of voyages")
                flight_number_list = print("\tEnter 3 for a list of flight numbers")
                voyage_sate = print("\tEnter 4 to see the state of the voyages for today")


                new_input = input("What you wanna do?: ")

            

        
