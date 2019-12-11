from model.VoyageM import Voyage
import csv

class VoyageIO:
    VOYAGE_FILE = "./files/voyage.csv"

    def __init__(self):
        self.__voyage_list = list()
    
    """def change_voyage(self, change, new):     # óklárað 
        change_index = self.CONSTANT_LIST.index(change.upper())

        with open(self.VOYAGE_FILE) as thefile:
            reader = csv.reader(thefile.readlines())

        with open(self.VOYAGE_FILE, "w", encoding= "Latin-1", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for line in reader:
                if line[0] == ssn:        # Á eftir að breyta ssn í eh annað .. 
                    line[change_index] = new
                    writer.writerow(line)
                    break
                else:
                    writer.writerow(line)
            writer.writerows(reader)"""

    def load_voyage_from_file(self):
        with open(self.VOYAGE_FILE, "r") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                voyage = Voyage(line["start of journey"],line["departure time out"],line["arriving abroad"],
                line["arrival time abroad"], line["departing to RVK"], line["departure time to RVK"],
                line["arrival time at RVK"], line["plane_insignia"], line["captain/pilot"], line["co-pilot"], 
                line["fsm"], line["fa1"],line["fa2"], line["flight_number"], line["status"])
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

    def Add_voyage_to_file(self, departure_time, arriving_abroad, arrival_time, departure_time_home, arrival_time_home, plane_insignia, captain, co_pilot, fsm, fa1, fa2, flight_number,status):
        with open(self.VOYAGE_FILE, "a", newline = " ") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Reykjavík", departure_time, arriving_abroad, arrival_time, 
            "Reykjavík", departure_time_home, arrival_time_home, plane_insignia, 
            captain, co_pilot, fsm, fa1, fa2, flight_number,status])


