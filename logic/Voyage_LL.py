from model.VoyageM import Voyage

from IO.employeeIO import EmployeeIO

#from IO.voyageIO import VoyageIO

import string

class VoyageLL():

    def __init__(self):
        #self.__io_voyage = VoyageIO
        pass

    def create_voyage(self, new_voyage):
        #self.__io_voyage.Add_voyage_to_file(new_voyage.split(","))
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
                if letter.isdigit() or letter in string.punctuation:
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
        if len(SSN) == 10:
            for letter in SSN:
                if letter.isalpha() or letter in string.punctuation:
                    return False
        else: 
            return False
        return True
        
        # Kalla á fallið check_if_exist
       

    def check_if_exist(self):
        # Validate-a að nafn starfsmanns sé á skrá
        # mögulega aðra hluti .. 
        # importa frá IO employee
        pass

        
    




    