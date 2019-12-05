from model.VoyageM import Voyage

class Voyage():
    def __init__(self, departing_from, departure_time, arriving_at, arrival_time, departure_time_home, arrival_time_home, aircraft_ID, captain, co_pilot, fsm, fa1, fa2, flight_number):
    
        self.__departing_from_out = departing_from   #The flight from rvk to destination
        self.__departure_time_out = departure_time
        self.__arriving_at_out = arriving_at
        self.__arrival_time_out = arrival_time

        self.__departing_from_home = arriving_at #The flight from destination to rvk
        self.__departing_time_home = departure_time_home
        self.__arriving_at_home = departing_from
        self.__arrival_time_home = arrival_time_home

        self.__aircraft_ID = aircraft_ID
        self.__captain = captain
        self.__co_pilot = co_pilot
        self.__fsm = fsm
        self.__fa1 = fa1
        self.__fa2 = fa2
        self.__flight_number = flight_number
    

    def __str__(self):
        pass


