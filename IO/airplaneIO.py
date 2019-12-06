from model.AirplaneM import Airplane
import csv

class AirplaneIO:
    AIRPLANE_FILE = "./files/employee.csv"

    def __init__(self):
        self.__airplane_list = list()

    def load_airplane_from_file(self):
        with open(self.AIRPLANE_FILE, "r") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                employee = Airplane(line["Manufacturer"],line["Type-ID"],line["Plane_insignia"],line["Model"])
                self.__airplane_list.append(employee)
        sorted_list = self.sort_to_display(self.__airplane_list)
        
        self.__employee_list = sorted_list

    def __str__(self):
        strengur = ''
        for airplane in self.__employee_list:
            strengur += airplane.__str__() + '\n'
        return strengur

    def sort_to_display(self, a_list):
        a_list.sort(key = lambda x: x.get_manufacturer())
        return a_list

    def Add_airplane_to_file(self,manufacturer, type_ID, plane_insignia, model):
        with open(self.AIRPLANE_FILE, "a", newline = " ") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([manufacturer,type_ID,plane_insignia,model])
