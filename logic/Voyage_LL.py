from model.VoyageM import Voyage
from IO.employeeIO import EmployeeIO
from datetime import datetime
import datetime
from IO.voyageIO import VoyageIO
from IO.destinationIO import DestinationIO
import string

class VoyageLL():

    def __init__(self):
        self.__io_voyage = VoyageIO()
        self.__employee = EmployeeIO()
        self.__destinatio = DestinationIO()

    def check_if_exists(self, check, num):
        destination_set = self.__io_voyage.get_set(num)
        for elements in destination_set:
            if check == elements:
                return False
        else: 
            return True


    def load_voyage_from_file(self):
        return self.__io_voyage.load_voyage_from_file()

    def make_flight_number(self,date,destination_number):
        flight_system = ["NA","XX","X"]
        flight_system[1] = destination_number
        flight_number1 = flight_system
        flight_number1[-1] = len(flight_list)*2
        flight_number2 = flight_system
        flight_number2 = len(flight_list) + 1
    
    def create_voyage(self, new_voyage):
        start_of_journey , departure_time_out, arriving_abroad, departure_time_home, aircraft_ID, captain, co_pilot, fsm, fa1, fa2= new_voyage.split(",")
        flight_time = self.__io_voyage.get_flight_time(arriving_abroad)
        hours, minutes = flight_time.split(".")
        flight_time = datetime.time(int(hours),int(minutes))
        arrival_time_abroad = departure_time_out + flight_time
        departing_to_RVK = "KEF"
        arrival_time_home = 0
        flight_number = 0
        captain = self.__io_voyage.transform_ssn_into_user_name(captain)
        co_pilot = self.__io_voyage.transform_ssn_into_user_name(co_pilot)
        fsm  = self.__io_voyage.transform_ssn_into_user_name(fsm)
        fa1 = self.__io_voyage.transform_ssn_into_user_name(fa1)
        fa2 = self.__io_voyage.transform_ssn_into_user_name(fa2)
        self.__io_voyage.Add_voyage_to_file(start_of_journey, departure_time_out, arriving_abroad, arrival_time_abroad, departing_to_RVK, departure_time_home, arrival_time_home, aircraft_ID, captain, co_pilot, fsm, fa1, fa2, flight_number)


    def change_voyage(self, des, date_time, change, new):
        #self.__io_voyage.change_voyage(new, change) 
        pass                                   
        

    def validate_employee(self):
        pass

    def validate_departure(self,departure):
        try:
            year,month,day,hours,minutes = departure.split("/")
            departure = datetime.datetime(int(year),int(month),int(day),int(hours),int(minutes))
            now = datetime.datetime.now()
            if now < departure:
                return True
        except ValueError:
            return False
        

    # Here comes validations form the former Flight_LL class

    def validate_departing_from(self, departing_from):   # Check if string only has alphabetical letters and is 3 letters long
        """ Validates whether "departing_from" is 3 letters long (e.g KEF) and that every letter is a part of the alphabet"""
        if len(departing_from) == 3:
            for letter in departing_from:
                if letter.isdigit() or letter in string.punctuation:
                    return False
        else:
            return False
        return True
    
    def validate_arriving_at(self, arriving_at):  # Check if string only has alphabetical letters and is 3 letters long
        """ Validates whether "arriving_at" is 3 letters long (e.g KEF) and that every letter is a part of the alphabet"""
        if len(arriving_at) == 3:
            for letter in arriving_at:
                if letter.isdigit() or letter in string.punctuation:
                    return False
        else:
            return False
        return True
       
    
    #def validate_arrival_time(self): # Þarf líklega ekki að validate-a, útfært sem datetime í UI
        #pass

    # def validate_aircraft_ID(self):  Þarf líklegast að import-a frá Airplane_LL
        # pass

    def validate_SSN(self, SSN):
        """ Validates that the Social security number (SSN) is 10 letters long and consists only of digits"""
        if SSN != "N/A":
            if self.check_if_exists(SSN):
                return True
            else: 
                return False
        return True
        
        # Kalla á fallið check_if_exist
       
