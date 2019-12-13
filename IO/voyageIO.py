from model.VoyageM import Voyage
from datetime import datetime
import datetime
import csv

class VoyageIO:
    VOYAGE_FILE = "./files/voyage.csv"
    EMPLOYEE_FILE = "./files/employee.csv"
    DESTINATION_FILE = "./files/destination.csv"
    HEADER = ""

    def __init__(self):
        self.__voyage_list = list()
        self.__voyage_set = set

    def get_voyage_list(self):
        return self.__voyage_list


    def get_all_voyages_for_employee(self,ssn):
        with open(self.VOYAGE_FILE, "r",encoding= "Latin-1") as the_file:
            reader = csv.reader(the_file)
            for line in reader:
                self.__voyage_set.add(line[num])
    def make_set(self,num):
        """Makes a set of all values in the num spot of the line"""
        with open(self.VOYAGE_FILE, "r",encoding= "Latin-1") as the_file:
            reader = csv.reader(the_file)
            for line in reader:
                self.__voyage_set.add(line[num])

    def get_set(self,num):
        self.make_set(num)
        return self.__voyage_set
    
    def get_flight_time(self,destination_name):
        """Goes through the destination file and finds the flight time from KEF to that destination"""
        with open(self.DESTINATION_FILE) as thefile:
            reader = csv.DictReader(thefile)
            for line in reader:
                if line["destination number"] == destination_name:
                    return line["flight time"]


    def load_voyage_from_file(self):
        """Makes a list of all the voyages in the voyage file"""
        with open(self.VOYAGE_FILE, "r") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                voyage = Voyage(line["start of journey"],line["departure time out"],line["arriving abroad"],
                line["arrival time abroad"],line["flight number out"], line["departing to RVK"], line["departure time to RVK"],
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
        """sorts the list by time"""
        a_list.sort(key = lambda x: x.get_departure_time_out())
        return a_list

    def transform_ssn_into_user_name(self,ssn):
        """Goes through the employee file finds the person that matches the ssn and writes out the user_name"""
        user_name = ""
        if ssn.upper() != "N/A":
            with open(self.EMPLOYEE_FILE, "r", encoding="Latin-1") as the_file:
                reader = csv.DictReader(the_file)
                for line in reader:
                    if line["SSN"] == ssn:
                        user_name =  line["User_name"]
        else:
            user_name = ssn.upper()

        return user_name

    def display_voyages_on_a_day(self,date):
        year,month,day = date.split("/")
        date = "{}-{}-{}".format(year,month,day)
        a = False
        with open(self.VOYAGE_FILE) as the_file:
            for line in csv.DictReader(the_file):
                if (line["departure time out"].split(" ")[0] == date or line["departure time to RVK"].split(" ")[0] == date) and (line["captain/pilot"] != "N/A" and line["co-pilot"] != "N/A" and line["fsm"] != "N/A"):
                    voyage = Voyage(line["start of journey"],line["departure time out"],line["arriving abroad"],
                    line["arrival time abroad"],line["flight number out"], line["departing to RVK"], line["departure time to RVK"],
                    line["arrival time at RVK"], line["plane_insignia"], line["captain/pilot"], line["co-pilot"], 
                    line["fsm"], line["fa1"],line["fa2"], line["flight_number"],"Fully staffed")
                    a = True
                    self.__voyage_list.append(voyage)
                if not a: 
                    voyage = Voyage(line["start of journey"],line["departure time out"],line["arriving abroad"],
                    line["arrival time abroad"],line["flight number out"], line["departing to RVK"], line["departure time to RVK"],
                    line["arrival time at RVK"], line["plane_insignia"], line["captain/pilot"], line["co-pilot"], 
                    line["fsm"], line["fa1"],line["fa2"], line["flight_number"],"Not fully staffed")
                    a = True
                    self.__voyage_list.append(voyage)

        sorted_list = self.sort_to_display(self.__voyage_list)
        self.__voyage_list = sorted_list

    def get_destination_id(self,destination_num):
        with open(self.DESTINATION_FILE) as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                if line["destination number"] == destination_num:
                    return line["destination id"]

    def make_flight_list(self,destination_num,date):

        destination_id = self.get_destination_id(destination_num)
        flight_list = list()
        with open(self.VOYAGE_FILE) as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                if line ["departure time out"].split(" ")[0] == date and line["arriving abroad"] == destination_id:
                    voyage = Voyage(line["start of journey"],line["departure time out"],line["arriving abroad"],
                    line["arrival time abroad"], line["departing to RVK"], line["departure time to RVK"],
                    line["arrival time at RVK"], line["plane_insignia"], line["captain/pilot"], line["co-pilot"], 
                    line["fsm"], line["fa1"],line["fa2"], line["flight_number"])
                    flight_list.append(voyage)

        return flight_list


    def Add_voyage_to_file(self, start_of_journey, departure_time_out, arriving_abroad, arrival_time_abroad, flight_number1, departing_to_RVK, departure_time_home, arrival_time_home, aircraft_ID, captain, co_pilot, fsm, fa1, fa2, flight_number2):
        """opens the voyage file and appends the new voyage to it"""
        
        with open(self.VOYAGE_FILE, "a", encoding="Latin-1", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([start_of_journey, departure_time_out, arriving_abroad, arrival_time_abroad, flight_number1, 
            departing_to_RVK, departure_time_home, arrival_time_home, aircraft_ID, 
            captain, co_pilot, fsm, fa1, fa2, flight_number2])


