from model.AirplaneM import Airplane
import csv

class AirplaneIO:
    AIRPLANE_FILE = "./files/airplane.csv"

    def __init__(self):
        self.__airplane_list = list()
        self.__airplane = Airplane("","","","")

    def load_airplane_from_file(self):
        with open(self.AIRPLANE_FILE, "r", encoding = "Latin-1") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                airplane = Airplane(line["Manufacturer"],line["Type-ID"],line["Plane_insignia"],line["Model"])
                self.__airplane_list.append(airplane)
        sorted_list = self.sort_to_display(self.__airplane_list)
        
        self.__airplane_list = sorted_list

    def __str__(self):
        return_str = ''
        for airplane in self.__airplane_list:
            return_str += airplane.__str__() + '\n'
        return return_str

    def sort_to_display(self, a_list):
        a_list.sort(key = lambda x: x.get_manufacturer())
        return a_list

    def Add_airplane_to_file(self,manufacturer, type_ID, plane_insignia, model):
        with open(self.AIRPLANE_FILE, "a",encoding = "Latin-1", newline = " ") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([manufacturer,type_ID,plane_insignia,model])

    def delete_plane(self, plane_insignia):
        plane_file = list()
        with open(self.AIRPLANE_FILE, "r", encoding="Latin-1") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                if line[0] != (self.__airplane.get_plane_insignia or []):
                    plane_file.append(line)

        with open(self.AIRPLANE_FILE, "a", encoding="Latin-1", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            for lists in plane_file:
                writer.writerow(lists)
