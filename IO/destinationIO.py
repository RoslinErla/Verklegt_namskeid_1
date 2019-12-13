from model.DestinationM import Destination
import csv

class DestinationIO:
    DESTINATION_FILE = "./files/destination.csv"
    CONSTANT_LIST = ["DESTINATION NUMBER", "DESTINATION NAME", "DESTINATION ID", "COUNTRY", "AIRPORT", "FLIGHT TIME", "DISTANCE", "EMERGENCY CONTACT", "EMERGENCY PHONE"]
    HEADER = "Destination number | Destination name | Destination ID | Country | Airport | Flight time | Distance | Emergency contact | Emergency phone"
    def __init__(self):
        self.__airplane_list = list()
        self.__destination_id_set = set()
        
    def make_set(self,num):
        with open(self.DESTINATION_FILE, "r",encoding= "Latin-1") as the_file:
            reader = csv.reader(the_file)
            for line in reader:
                self.__destination_id_set.add(line[num])

    def get_set(self,num):
        self.make_set(num)
        return self.__destination_id_set

    def load_destination_from_file(self):
        print(self.HEADER)
        with open(self.DESTINATION_FILE, "r") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                employee = Destination(line["destination number"],line["destination name"],line["destination id"],line["country"],line["airport"],line["flight time"],line["distance"],line["emergency contact"],line["emergency phone"])
                self.__airplane_list.append(employee)
        sorted_list = self.sort_to_display(self.__airplane_list)
        
        self.__destination_list = sorted_list

    def __str__(self):
        strengur = ''
        for destination in self.__destination_list:
            strengur += destination.__str__() + '\n'
        self.__airplane_list = list()
        return strengur

    def sort_to_display(self, a_list):
        a_list.sort(key = lambda x: x.get_destination_num())
        return a_list

    def Add_destination_to_file(self, destination_num, destination_name, destination_id, country, airport, flight_time, distance, emergency_contact, emergency_phone):
        with open(self.DESTINATION_FILE, "a", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([destination_num, destination_name, destination_id, country, airport, flight_time, distance, emergency_contact, emergency_phone])


    def change_destination(self, des, change, new):
        change_index = self.CONSTANT_LIST.index(change.upper())

        with open(self.DESTINATION_FILE) as thefile:
            reader = csv.reader(thefile.readlines())

        with open(self.DESTINATION_FILE, "w", encoding = "Latin-1", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for line in reader:
                if line[2] == des.upper():
                    line[change_index] = new
                    writer.writerow(line)
                    break
                else:
                    writer.writerow(line)
            writer.writerows(reader)
