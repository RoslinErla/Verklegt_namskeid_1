from model.flightM import Flight
import string


class FlightLL(Flight):

    def __init__(self, inp):
        # self.__IOAPI = IOAPI()
        self.inp = inp

    def add_flight(self):
        pass

    def change_flight(self):
        pass

    def validate_departing_from(self, departing_from):   # Check if string only has alphabetical letters and is 3 letters long
        if type(departing_from) == str:
            for word in departing_from:
                for letter in word:
                    if letter.isalpha and len(self.inp) == 3:
                        return True

    #def validate_departure_time(self):
        #pass

    def validate_arriving_at(self, arriving_at):  # Check if string only has alphabetical letters and is 3 letters long
        if type(arriving_at) == str:
            for word in arriving_at:
                for letter in word:
                    if letter.isalpha and len(self.inp) == 3:
                        return True
    
    #def validate_arrival_time(self):
        #pass

    # def validate_aircraft_ID(self):  Þarf líklegast að import-a frá Airplane_LL
        # pass

    def validate_captain(self, captain):  # Check if the id is 10 numbers
        if len(captain) == 10:
            return True


    def validate_co_pilot(self, co_pilot): # Check if the id is 10 numbers
        if len(co_pilot) == 10:
            return True

    def validate_fsm(self, fsm): # Check if the id is 10 numbers
        if len(fsm) == 10:
            return True
        

    def validate_fa1(self, fa1): # Check if the id is 10 numbers
        if len(fa1) == 10:
            return True

    def validate_fa2(self, fa2): # Check if the id is 10 numbers
        if len(fa2) == 10:
            return True

    def validate_flight_number(self, flight_number): # Check if the id is 10 numbers
        if len(flight_number) == 10:
            return True






