from model.VoyageM import Voyage

class Voyage(Flight):
    def __init__(self, employee, flight_out, flight_home, departing_from, departure_time, arriving_at, arrival_time, aircraft_ID, captain, co_pilot, fsm, fa1, fa2, flight_number):
        self.employee = employee
        self.flight_out = flight_out   # useless ?
        self.flight_home = flight_home  # useless ? 
    
        self.__departing_from = departing_from   # Here comes the variables from flightM
        self.__departure_time = departure_time
        self.__arriving_at = arriving_at
        self.__arrival_time = arrival_time
        self.__aircraft_ID = aircraft_ID
        self.__captain = captain
        self.__co_pilot = co_pilot
        self.__fsm = fsm
        self.__fa1 = fa1
        self.__fa2 = fa2
        self.__flight_number = flight_number
    

    def __str__(self):
        pass


