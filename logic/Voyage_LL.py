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
        """Checks if a specific destination element already exists in other destinations"""
        destination_set = self.__io_voyage.get_set(num)
        for elements in destination_set:
            if check == elements:
                return False
        else: 
            return True

    def load_voyage_from_file(self):
        self.__io_voyage.load_voyage_from_file()
        return str(self.__io_voyage)

    def make_flight_number(self,date,destination_number):
        """Gets a list of all the flights that day to that destination. Makes the flight number"""
        flight_list = self.__io_voyage.make_flight_list(destination_number, date)
        flight_system = ["NA","XX","X"]

        flight_system[1] = destination_number

        if len(flight_list) == 0:
            length = len(flight_list)
        else:
            length = len(flight_list) + 1 #The voyage we are making would be the next element in that list

        flight_number1 = flight_system.copy()
        flight_number1[-1] = str(length*2)
        flight_number2 = flight_system.copy()
        flight_number2[-1] = str(length * 2 + 1)

        flight_number1 = "".join(flight_number1)
        flight_number2 = "".join(flight_number2)

        return flight_number1,flight_number2
    
    def create_voyage(self, new_voyage):
        start_of_journey , departure_time_out, arriving_abroad, aircraft_ID, captain, co_pilot, fsm, fa1, fa2= new_voyage.split(",")

        year,month,day,hour,minutes = departure_time_out.split("/")
        date = "{}-{}-{}".format(year,month,day)
        departure_time_out_datetime = datetime.datetime(int(year),int(month),int(day),int(hour),int(minutes))
        
        flight_time = self.__io_voyage.get_flight_time(arriving_abroad)

        hours, minutes = flight_time.split(".")

        arrival_time_abroad = departure_time_out_datetime + datetime.timedelta(hours = int(hours), minutes = int(minutes))
        departing_to_RVK = "KEF"
        departure_time_home = (arrival_time_abroad + datetime.timedelta(hours = 1))
        arrival_time_home = departure_time_home + datetime.timedelta(hours= int(hours), minutes = int(minutes))

        flight_number1,flight_number2 = self.make_flight_number(date,arriving_abroad)

        captain = self.__io_voyage.transform_ssn_into_user_name(captain)
        co_pilot = self.__io_voyage.transform_ssn_into_user_name(co_pilot)
        fsm  = self.__io_voyage.transform_ssn_into_user_name(fsm)
        fa1 = self.__io_voyage.transform_ssn_into_user_name(fa1)
        fa2 = self.__io_voyage.transform_ssn_into_user_name(fa2)
        self.__io_voyage.Add_voyage_to_file(start_of_journey, departure_time_out_datetime, arriving_abroad, arrival_time_abroad,flight_number1, departing_to_RVK, departure_time_home, arrival_time_home, aircraft_ID, captain, co_pilot, fsm, fa1, fa2, flight_number2)


    def change_voyage(self, des, date_time, change, new):
        #self.__io_voyage.change_voyage(new, change) 
        pass                                   
        

    def validate_departure(self,departure):
        try:
            year,month,day,hours,minutes = departure.split("/")
            departure = datetime.datetime(int(year),int(month),int(day),int(hours),int(minutes))
            now = datetime.datetime.now()
            if now < departure:
                if validate_departure_availability(self):
                    return True
        except ValueError:
            return False
        
    def validate_departure_availability(self):
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
    
    def validate_arriving_at(self, arriving_at):  # Check if string only has alphabetical letters and is 3 letters long
        """ Validates whether "arriving_at" is 3 letters long (e.g KEF) and that every letter is a part of the alphabet"""
        if len(arriving_at) == 3:
            for letter in arriving_at:
                if letter.isdigit() or letter in string.punctuation:
                    return False
        else:
            return False
        return True
       

    def show_voyages_on_a_day(self, date):
        self.__io_voyage.display_voyages_on_a_day(date)
        return str(self.__io_voyage)

    def show_voyages_in_a_week(self,date):
        self.__io_voyage.display_voyages_on_a_week(date)
        return str(self.__io_voyage)

       
