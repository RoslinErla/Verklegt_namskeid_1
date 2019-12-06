from model.VoyageM import Voyage

import string

class VoyageLL(Voyage):

    def __init__(self):
        pass  

    def create_voyage(self):
        pass

    def change_voyage(self):
        pass

    def validate_employee(self):
        pass

    def validate_flight_out(self):
        pass

    def validate_flight_home(self):
        pass

    # Here comes validations form the former Flight_LL class

    def validate_departing_from(self, departing_from):   # Check if string only has alphabetical letters and is 3 letters long
        """ Validates whether "departing_from" is 3 letters long (e.g KEF) and that every letter is a part of the alphabet"""
        if len(departing_from) == 3:
            for letter in departing_from:
                if letter.isdigit or letter in string.punctuation:
                    return False
        else:
            return False
        return True
    
                    
    #def validate_departure_time(self):  # Þarf líklega ekki að validate-a, útfært sem datetime í UI
        #pass

    def validate_arriving_at(self, arriving_at):  # Check if string only has alphabetical letters and is 3 letters long
        """ Validates whether "arriving_at" is 3 letters long (e.g KEF) and that every letter is a part of the alphabet"""
        if len(arriving_at) == 3:
            for letter in arriving_at:
                if letter.isdigit or letter in string.punctuation:
                    return False
        else:
            return False
        return True
       
    
    #def validate_arrival_time(self): # Þarf líklega ekki að validate-a, útfært sem datetime í UI
        #pass

    # def validate_aircraft_ID(self):  Þarf líklegast að import-a frá Airplane_LL
        # pass

    def validate_captain(self, captain):  # Check if the id is 10 numbers
        """ Validates that the captain's SSN is 10 letters long"""
        if len(captain) == 10:
            return True
       


    def validate_co_pilot(self, co_pilot): # Check if the id is 10 numbers
        """ Validates that the co-pilot's SSN is 10 letters long"""
        if len(co_pilot) == 10:
            return True
        

    def validate_fsm(self, fsm): # Check if the id is 10 numbers
        """ Validates that the flight service manager's SSN is 10 letters long"""
        if len(fsm) == 10:
            return True
        
        
    def validate_fa1(self, fa1): # Check if the id is 10 numbers
        """ Validates that the flight servant's SSN is 10 letters long"""
        if len(fa1) == 10:
            return True

    def validate_fa2(self, fa2): # Check if the id is 10 numbers
        """ Validates that the flight servant's SSN is 10 letters long"""
        if len(fa2) == 10:
            return True

    def validate_flight_number(self, flight_number): # Check if the id is 10 numbers
        """ Validates that the flight number is 10 letters long"""
        if len(flight_number) == 10:
            return True




    