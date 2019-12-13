from model.AirplaneM import Airplane
import csv

class AirplaneIO:
    AIRPLANE_FILE = "./files/airplane.csv"
    VOYAGE_FILE = "./files/voyage.csv"
    CONSTANTS_LIST = ["MANUFACTURER", "TYPE-ID", "PLANE_INSIGNIA", "MODEL", "STATUS"]
    HEADER = "{:12} | {:15} | {:15} | {:6}".format("Manufacturer", "Type-ID", "Plane_Insignia", "Model")

    def __init__(self):
        self.__airplane_list = list()
        self.__airplane = Airplane()
        self.__airplane_set = set()

    def get_airplane_list(self):
        return self.__airplane_list

    def make_set(self,num):
        with open(self.AIRPLANE_FILE, "r",encoding= "Latin-1") as the_file:
            reader = csv.reader(the_file)
            for line in reader:
                self.__airplane_set.add(line[num])

    def get_set(self,num):
        self.make_set(num)
        return self.__airplane_set
        
    def check_if_not_available(self,date):
        airplane_list = list()
        year,month,day,hours,minutes = date.split("/")
        date = "{}-{}-{}".format(year,month,day)
        with open(self.VOYAGE_FILE) as the_file:
            voyage_reader = csv.DictReader(the_file)
            for line in voyage_reader:
                if line["departure time out"].split(" ")[0] == date:
                    with open(self.AIRPLANE_FILE) as other_file:
                        airplane_reader = csv.DictReader(other_file)
                        for elements in airplane_reader:
                            if line["plane_insignia"] == elements["Plane insignia"]:
                                airplane = Airplane(elements["Manufacturer"],elements["Type-ID"],elements["Plane_Insignia"],elements["Model"])
                                airplane_list.append(airplane)
        return airplane_list

    def check_if_available(self,date):
        unavailable_list = self.check_if_not_available(date)
        available_list = list() 
        with open(self.AIRPLANE_FILE) as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                airplane = Airplane(line["Manufacturer"],line["Type-ID"],line["Plane_Insignia"],line["Model"])
                if airplane not in unavailable_list:
                    available_list.append(airplane)

        self.__airplane_list = available_list


    def load_airplane_from_file(self):
        print(self.HEADER)
        with open(self.AIRPLANE_FILE, "r", encoding = "Latin-1") as the_file:
            reader = csv.DictReader(the_file)
            for line in reader:
                airplane = Airplane(line["Manufacturer"],line["Type-ID"],line["Plane_Insignia"],line["Model"])
                self.__airplane_list.append(airplane)
        sorted_list = self.sort_to_display(self.__airplane_list)
        
        self.__airplane_list = sorted_list

    def __str__(self):
        return_str = ''
        for airplane in self.__airplane_list:
            return_str += airplane.__str__() + '\n'
        self.__airplane_list = list()
        return return_str

    def sort_to_display(self, a_list):
        a_list.sort(key = lambda x: x.get_manufacturer())
        return a_list

    def Add_airplane_to_file(self, manufacturer, type_ID, plane_insignia, model):
        with open(self.AIRPLANE_FILE, "a",encoding = "Latin-1", newline = "") as csvfile:
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
        
    def change_airplane(self,plane_insignia, change, new):
        change_index = self.CONSTANTS_LIST.index(change.upper())

        with open(self.AIRPLANE_FILE) as thefile:
            reader = csv.reader(thefile.readlines())

        with open(self.AIRPLANE_FILE, "w", encoding="Latin-1",newline="") as csvfile:
            writer = csv.writer(csvfile)
            for line in reader:
                if line[2] == plane_insignia.upper():
                    line[change_index] = new
                    writer.writerow(line)
                    break
                else: 
                    writer.writerow(line)
            writer.writerows(reader)

    # def display_status(self,date):
    #     reader 
    #     reader
    #     if first: 
            