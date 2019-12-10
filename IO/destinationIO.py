from model.DestinationM import Destination
import csv

class DestinationIO:
    DESTINATION_FILE = "./files/destination.csv"
    CONSTANT_LIST = ["DESTINATION NAME", "DESTINATION ID", "COUNTRY", "AIRPORT", "FLIGHT TIME", "DISTANCE", "EMERGENCY CONTACT", "EMERGENCY PHONE"]

    def __init__(self):
        self.__airplane_list = list()

    def load_destination_from_file(self):
        with open(self.DESTINATION_FILE, "r") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                employee = Destination(line["destination name"],line["destination id"],line["country"],line["airport"],line["flight time"],line["distance"],line["emergency contact"],line["emergency phone"])
                self.__airplane_list.append(employee)
        sorted_list = self.sort_to_display(self.__airplane_list)
        
        self.__employee_list = sorted_list

    def __str__(self):
        strengur = ''
        for employee in self.__employee_list:
            strengur += employee.__str__() + '\n'
        return strengur

    def sort_to_display(self, a_list):
        a_list.sort(key = lambda x: x.get_destination_name())
        return a_list

    def Add_destination_to_file(self,destination_name, destination_id, country, airport, flight_time, distance, emergency_contact, emergency_phone):
        with open(self.DESTINATION_FILE, "a", newline = " ") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([destination_name, destination_id, country, airport, flight_time, distance, emergency_contact, emergency_phone])

    def change_destination(self, destination_id, change, new):
        change_index = self.CONSTANT_LIST.index(change.upper())

        with open(self.DESTINATION_FILE) as thefile:
            reader = csv.DictReader(thefile.readlines())

        with open(self.DESTINATION_FILE, "w") as csvfile:
            writer = csv.writer(csvfile)
            for line in reader:
                if line[1] == destination_id.upper():
                    writer.writerow(line[change_index], new)
