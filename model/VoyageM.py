

class Voyage():
    def __init__(self, start_of_journey = "", departure_time_out = "", arriving_abroad = "", arrival_time_abroad = "",fligth_number_out = "", departing_to_RVK = "", departure_time_home = "", arrival_time_home = "", aircraft_ID = "", captain = "", co_pilot = "", fsm = "", fa1 = "", fa2 = "", flight_number = "",status = ""):
    
        self.__departing_from_out = start_of_journey   #The flight from rvk to destination
        self.__departure_time_out = departure_time_out
        self.__arriving_at_out = arriving_abroad
        self.__arrival_time_out = arrival_time_abroad
        self.__flight_number_out = fligth_number_out

        self.__departing_from_home = departing_to_RVK #The flight from destination to rvk
        self.__departing_time_home = departure_time_home
        self.__arrival_time_home = arrival_time_home

        self.__aircraft_ID = aircraft_ID
        self.__captain = captain
        self.__co_pilot = co_pilot
        self.__fsm = fsm
        self.__fa1 = fa1
        self.__fa2 = fa2
        self.__flight_number = flight_number
        self.__status = status
    
    def __str__(self):
        return "{} | {} |{} | {} |{} | {} | {} |{} | {} | {} | {} | {} | {} | {} | {} | {}".format(self.__departing_from_out, self.__departure_time_out, self.__arriving_at_out,self.__arrival_time_out,self.__flight_number_out,self.__departing_from_home, self.__departing_time_home,self.__arrival_time_home,self.__aircraft_ID,self.__captain,self.__co_pilot,self.__fsm,self.__fa1,self.__fa2,self.__flight_number,self.__status)
  
    def get_departure_time_out(self):
        return self.__departure_time_out


