from model.VoyageM import Voyage
import csv

class VoyageIO:
    VOYAGE_FILE = "./files/voyage.csv"
    EMPLOYEE_FILE = "./files/employee.csv"
    DESTINATION_FILE = "./files/destination.csv"

    def __init__(self):
        self.__voyage_list = list()
    
    def get_flight_time(self,destination_name):
        with open(self.DESTINATION_FILE) as thefile:
            reader = csv.DictReader(thefile)
            for line in reader:
                if line["destination name"] == destination_name:
                    return line["flight time"]



    def load_voyage_from_file(self):
        with open(self.VOYAGE_FILE, "r") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                voyage = Voyage(line["start of journey"],line["departure time out"],line["arriving abroad"],
                line["arrival time abroad"], line["departing to RVK"], line["departure time to RVK"],
                line["arrival time at RVK"], line["plane_insignia"], line["captain/pilot"], line["co-pilot"], 
                line["fsm"], line["fa1"],line["fa2"], line["flight_number"])
                self.__voyage_list.append(voyage)
        sorted_list = self.sort_to_display(self.__voyage_list)
        self.__voyage_list = sorted_list

    def __str__(self):
        return_str = ""
        for voyage in self.__voyage_list:
            return_str += voyage.__str__() + '\n'
        return return_str

    def sort_to_display(self,a_list):
        a_list.sort(key = lambda x: x.get_departure_time_out())
        return a_list

    def transform_ssn_into_user_name(self,ssn):
        user_name = ""
        if ssn != "N/A":
            with open(self.EMPLOYEE_FILE, "r", encoding="Latin-1") as the_file:
                reader = csv.DictReader(the_file)
                for line in reader:
                    if line["SSN"] == ssn:
                        user_name =  line["User_name"]

        else:
            user_name = ssn

        return user_name

    def Add_voyage_to_file(self, start_of_journey, departure_time_out, arriving_abroad, arrival_time_abroad, departing_to_RVK, departure_time_home, arrival_time_home, aircraft_ID, captain, co_pilot, fsm, fa1, fa2, flight_number):
        with open(self.VOYAGE_FILE, "a", encoding="Latin-1", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([start_of_journey, departure_time_out, arriving_abroad, arrival_time_abroad, 
            departing_to_RVK, departure_time_home, arrival_time_home, aircraft_ID, 
            captain, co_pilot, fsm, fa1, fa2, flight_number])


