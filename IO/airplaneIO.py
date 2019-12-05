from model.AirplaneM import Airplane
import csv

class AirplaneIO:
    AIRPLANE_FILE = "./files/airplane.csv"

    def __init__(self):
        pass

    def load_airplane_from_file_alphabetically(self):
        pass

    def load_airplane_from_file_by_use(self):
        pass

    def Add_airplane_to_file(self,manufacturer, type_ID, plane_insignia, model):
        with open(self.AIRPLANE_FILE, "a", newline = " ") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([manufacturer,type_ID,plane_insignia,model])
