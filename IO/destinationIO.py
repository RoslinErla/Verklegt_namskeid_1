from model.DestinationM import Destination
import csv

class DestinationIO:
    DESTINATION_FILE = "./files/destination.csv"

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
        a_list.sort(key = lambda x: x.get_manufacturer())
        return a_list

    def Add_destination_to_file(self, country, airport, flight_time, distance, emergency_contact, emergency_phone):
        with open(self.DESTINATION_FILE, "a", newline = " ") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([country, airport, flight_time, distance, emergency_contact, emergency_phone])
