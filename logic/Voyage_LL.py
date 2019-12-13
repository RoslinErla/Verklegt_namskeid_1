from model.VoyageM import Voyage
from IO.employeeIO import EmployeeIO
from datetime import datetime
import datetime
from IO.voyageIO import VoyageIO
import string

class VoyageLL():

    def __init__(self):
        self.__io_voyage = VoyageIO()
        self.__employee = EmployeeIO()


    def make_flight_number(self,date,destination_number):
        flight_system = ["NA","XX","X"]
        flight_system[1] = destination_number


        pass
    

    def create_voyage(self, new_voyage):
        start_of_journey , departure_time_out, arriving_abroad, departure_time_home, aircraft_ID, captain, co_pilot, fsm, fa1, fa2= new_voyage.split(",")
        flight_time = self.__io_voyage.get_flight_time(arriving_abroad)
        hours, minutes = flight_time.split(".")
        flight_time = datetime.time(int(hours),int(minutes))
        arrival_time_abroad = departure_time_out + flight_time
        departing_to_RVK = 0
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

    def validate_flight_out(self):
        pass

    def validate_flight_home(self):
        pass

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
    
                    
    #def validate_departure_time(self, a_time):  # Þarf líklega ekki að validate-a, útfært sem datetime í UI
       



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
            if self.check_if_exist(SSN):
                return True
            else: 
                return False
        return True
        
        # Kalla á fallið check_if_exist
       

    def check_if_exist(self,check):
        employee_set = self.__employee.get_set()
        for elements in employee_set:
            if check == elements:
                return True
        else: 
            return False
