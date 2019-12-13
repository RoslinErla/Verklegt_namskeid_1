from logic.Voyage_LL import VoyageLL
from model.VoyageM import Voyage
from IO.voyageIO import VoyageIO
from logic.Destination_LL import DestinationLL
from IO.destinationIO import DestinationIO
from UI.Destination_UI import DestinationUI
from logic.Employee_LL import EmployeeLL
from IO.employeeIO import EmployeeIO
from logic.Airplane_LL import AirplaneLL
from IO.airplaneIO import AirplaneIO
from datetime import datetime
import datetime
from datetime import date
import string

class VoyageUI():

    def __init__(self):
        self.__ll_voyage = VoyageLL()
        self.__ll_destination = DestinationLL()
        self.__ui_destination = DestinationUI()
        self.__ll_employee = EmployeeLL()
        self.__ll_airplane = AirplaneLL()

    def voyage_menu(self): 
        """ The user can choose between the create, change and display options in the system"""
        action = ""
        leave = ""
        while leave != "q":
            print("The following actions are possible: ")
            print("\tEnter 1 to create a voyage within the system.")
            print("\tEnter 2 to change staff on voyages already within the system.")
            print("\tEnter 3 to display voyages within the system.")
            print("Enter b or q to got to the main menu.")
           
            action = input("Please enter your command: ").lower()

            if action == "1":
                leave = self.new_voyage()
            
            if action == "2":
                leave = self.change_menu()
            
            if action == "3":
                leave = self.display_menu()
        
            if action == "q" or action == "b":
                break
                        
        
    def change_menu(self):
        """After the user has chosen the "change" option, he has two new options"""
        action = ""
        while leave != "q":
            action = input("Please enter your commmand: ").lower()
        
            if action == "1":
                action = self.change_voyage_state()
        
            if action == "2":
                action = self.__ui_destination.change_contact()
        
            if action == 'b':
                self.voyage_menu() 
        
            if action == 'q':
                return "q"

    def new_voyage(self):
        """The user has chosen to create a new voyage"""
        action = ""
        new_voyage = "KEF,"
        
        print('Enter "b" to go back and "q" to got to the main menu.')
 
        while action != "q":
            a = self.__ll_voyage.load_voyage_from_file()
            print(a)
            print()
            date = input("Enter the departure time from Iceland (year(YYYY)/month(0-12)/day(0-31)/hour(0-23)/minutes(0-59): ")
            action = date
            if action.lower() == 'b' or action.lower() == "q":
                return "q"

            while not self.__ll_voyage.validate_departure(action):
                print("Input is invalid!")
                action = input("Enter the departure time from Iceland (year(YYYY)/month(0-12)/day(0-31)/hour(0-23)/minutes(0-59): ")
                if action.lower() == 'b' or action.lower() == "q":
                    return "q"

            new_voyage += action + ","
            
            
            a = self.__ll_destination.load_destination_from_file()
            print(a)
            action = input("Enter the destination number: ")
            print()
            if action.lower() == 'b' or action.lower() == "q":
                return "q"

            while not self.__ll_destination.check_if_exists(action,0):
                print("Input is invalid!")
                self.__io_destination.load_destination_from_file()
                print(self.__io_destination)
                action = input("Enter the destination: ")
                print()
                if action.lower() == 'b' or action.lower() == "q":
                    return "q"

            new_voyage += action + ","

            available_list = self.__ll_airplane.check_if_available(date)
            print(available_list)
            plane_insignia = input("Enter the plane insignia of the airplane: ")
            action = plane_insignia
            print()
            if action.lower() == 'b' or action.lower() == "q":
                return "q"
            while not self.__ll_airplane.check_if_in_available(date,action):
                print("Input is invalid!")
                plane_insignia = input("Enter the plane insignia of the airplane: ")
                action = plane_insignia
                print()
                if action.lower() == 'b' or action.lower() == "q":
                    return "q"
            new_voyage += action + ","

            a = self.__ll_employee.check_if_available(date,"captain")
            print(a)
            print()
            action =  input("Enter the captain's SSN (0000000000): ")         # User inputs the SSN for the captain
            if action.lower() == 'b' or action.lower() == "q":
                return "q"
            while not self.__ll_employee.check_if_in_available(date,"captain",action):
                print("Input is invalid")
                a = self.__ll_employee.check_if_available(date,"captain")
                print(a)
                action = input("Enter the captain's SSN (0000000000): ")
                if action.lower() == 'b' or action.lower() == "q":
                    return "q"

            new_voyage += action + ","


            a = self.__ll_employee.check_if_available(date,"co-pilot")
            print(a)
            print()
            action = input("Enter the co-pilot's SSN (0000000000): ")      # User inputs the SSN for the co-pilot
            if action == 'b' or action.lower() == "q":
                return "q"
            while not self.__ll_employee.check_if_in_available(date,"co-pilot",action):
                print("Input is invalid")
                a = self.__ll_employee.check_if_available(date,"co-pilot")
                print(a)
                print()
                action = input("Enter the co-pilot's SSN (0000000000): ")
                if action.lower() == 'b'or action.lower() == "q":
                    return "q"

            new_voyage += action + ","
            

            a = self.__ll_employee.check_if_available(date,"flight service manager")
            print(a)

            print()
            action = input("Enter the flight service manager's SSN (0000000000): ")  # User inputs the SSN for the fsm
            if action.lower() == 'b' or action.lower() == "q":
                return "q"
            while not self.__ll_employee.check_if_in_available(date,"flight service manager",action):
                print("Input is invalid")
                a = self.__ll_employee.check_if_available(date,"flight service manager")
                print(a)
                print()
                action = input("Enter the flight service manager's SSN (0000000000): ")
                if action.lower() == 'b' or action.lower() == "q":
                    return "q"

            new_voyage += action + ","

            a = self.__ll_employee.check_if_available(date,"flight attendant")
            print(a)
            print()            
            action = input("Enter the first flight attendant SSN (0000000000): ")   # User inputs the SSN for the first flight attendant
            if action.lower() == 'b' or action.lower() =="q":
                return "q"
            while not self.__ll_employee.check_if_in_available(date,"flight attendant",action):
                print("Input is invalid")
                action = input("Enter the first flight servant's SSN (0000000000): ")
                if action == 'b' or action.lower() == "q":
                    return "q"

            new_voyage += action + ","
            
            
            a = self.__ll_employee.check_if_available(date,"flight attendant")
            print(a)
            print()            
            action = input("Enter the first flight attendant SSN (0000000000): ")   # User inputs the SSN for the first flight attendant
            if action.lower() == 'b' or action.lower() =="q":
                return "q"
            while not self.__ll_employee.check_if_in_available(date,"flight attendant",action):
                print("Input is invalid")
                action = input("Enter the first flight servant's SSN (0000000000): ")
                if action == 'b' or action.lower() == "q":
                    return "q"

            new_voyage += action
            self.__ll_voyage.create_voyage(new_voyage)   

            action = input("Do you want to create another voyage? (y/n): ").lower()
            if action == "n":  # virkar ekki!
                return "q"
            
    def display_menu(self):
        """After the user has chosen the "display" option, he has three new options"""
        action = ""
        leave = ''
        while leave != "q":
            print("\tEnter 1 for a daily list of voyages")
            print("\tEnter 2 for a list of flight numbers")
            print("\tEnter 3 to see the state of the voyages for today")
            print('Enter "b" to go back and "q" to got to the main menu.')
            action = input("Please enter your commmand: ").lower()
        
            if action == "1":
                action = self.daily_list()
        
            if action == "2":
                action = self.flight_numbers()
        
            if action == "3":
                action = self.daily_voyage_state()
        
            if action == 'b':
                self.voyage_menu() 
        
            if action == 'q':
                return "q"
                  

                          
    def change_voyage_state(self):                                      
        """The user has chosen to change the status of the voyage"""     
        print('Enter "b" to go back and "q" to got to the main menu.')
        action = ""
        voyage_state = ""
        while True: 
            print()
            self.__io_destination.load_destination_from_file()
            print(self.__io_destination)
            print()
            des = input("Enter destination: ")             # vantar validate
            print()
            if des == 'b':
                self.change_menu()
            if des == 'q':
                return "q"
            while not self.__ll_destination.validate_destination_name(action):
                print("Input is invalid!")
                self.__io_destination.load_destination_from_file()
                print(self.__io_destination)
                action = input("Enter the destination: ")
                print()
                if action == 'b':
                    self.display_menu()
                if action == 'q':
                    return "q"
            voyage_state += action
            
            #date_time = input("Enter date and time: ")
            #if date_time == 'b':
                #self.change_menu()
            #if date_time == 'q':
                #return "q"
            change = input("Please enter what you wish to change: ")
            if change == "q":
                return "q"
            if change == "b":
                self.change_menu()
            new = input("Please enter the new entry for {}".format(change))
            if new == "q":
                return "q"
            if new == "b":
                self.change_menu()
            print()
            self.__ll_destination.change_destination(des, change, new)       #(des, change, new)  

            action = input("Do you want to change another voyage status? (y)es or (n)o: " ).lower()
            if action == "n":
                return "q"                          

    def daily_list(self):
        """The user has chosen to have a list of voyages for a given day displayed"""
        action = ""
        display_voyages = ""

        print('Enter "b" to go back and "q" to got to the main menu.')
       
        while True:                                                       # ..og maður ýtir á q ferð maður bara til baka í voyage_menu...ekki main menu 
            action = input("Enter a date: ")
            if action == 'b':
                self.display_menu()
            if action == 'q':
                return "q"
            while not self.__ll_destination.validate_distance(action):       # Nota distance núna því bara tölur MUNA :Breyta í DATETIME validated
                print("Input is invalid")
                action = input("Enter a date: ")
                if action == 'b':
                    self.display_menu()
                if action == 'q':
                    return "q"
            display_voyages += action
            
        
        # Birta listannn ! 
    
    # def flight_numbers(self):
    #     """The user has chosen to have a list of flight numbers for a given date displayed""" 
    #     action = ""
    #     display_numbers = ""
    #     print('Enter "b" to go back and "q" to got to the main menu.')  # fer líka bara til baka úr "Enter destination" í voyage menu með q 
    #     while True:                                                      # En þá er hægt að ýta aftur á q og þá fer maður í main menu...
    #         action = input("Enter destination: ")
    #         if action == 'b':
    #             self.display_menu()
    #         if action == 'q':
    #             return "q"
    #         while not self.__ll_destination.validate_country_name(action):   # Sýna flugnúmer beggja flugferða þegar vinnuferðir eru listaðar.
    #             print("Input is invalid")
    #             action = input("Enter destination: ")
    #         display_numbers += action
    #         if action == 'b':
    #             self.display_menu()
    #         if action == 'q':
    #             return "q"
            
    #         action = input("Enter a date: ")
    #         if action == 'b':
    #             self.display_menu()
    #         if action == 'q':
    #             return "q"
    #         while not self.__ll_destination.validate_distance(action):       # Nota distance núna því bara tölur MUNA :Breyta í DATETIME validated
    #             print("Input is invalid")
    #             action = input("Enter a date: ")
    #         display_numbers += action
    #         if action == 'b':
    #             self.display_menu()
    #         if action == 'q':
    #             return "q"
            
        # Birta lista flugnúmera fyrir innslegna dagsetningu
        
    def daily_voyage_state(self):
        """The user has chosen to have a list of voyage's status (finished, arrived or cancelled) displayed """
        action = ""
        display_state = ""
        print('Enter "b" to go back and "q" to got to the main menu.')      # Þegar maður er búinn að velja "see the state of the voyages.." og kemur "Enter date" ..
                                                          # ..og maður ýtir á q ferð maður bara til baka í voyage_menu...ekki main menu 
        action = input("Enter a date: ")                                 # og ef maður velur b í Enter date og fer svo aftur inn og velur q þá fær maður input is invalid!
        if action == 'b':
            self.display_menu()
        if action == 'q':
            return "q"
        while not self.__ll_destination.validate_distance(action):       # Nota distance núna því bara tölur MUNA :Breyta í DATETIME validated
            print("Input is invalid")
            action = input("Enter a date: ")
            if action == 'b': 
                self.display_menu()                  
            if action == 'q':                        
                return "q"
        display_state += action                   # a) lokið, b) lent ytra, c) í loftinu eða d) ekki hafin
                                   #  þarf að breyta strengnum í hlut, t.a.m. með dateutil.parser,

        # VANTAR Birta lista vinnuferða þar sem sést hvaða ferðum er lokið, lent ytra og eða felld niður

        




    






        

        

            



 
      

        
