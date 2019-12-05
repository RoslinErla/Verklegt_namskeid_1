from model.voyageM import voyage
import csv

class VoyageIO:
    VOYAGE_FILE = "./files/voyage.csv"

    def __init__(self):
        pass

    def load_voyage_from_file_alphabetically(self):
        pass

    def load_voyage_from_file_by_status(self):
        pass

    def Add_voyage_to_file(self, departure_time, arriving_abroad, arrival_time, departure_time_home, arrival_time_home, plane_insignia, captain, co_pilot, fsm, fa1, fa2, flight_number):
        with open(self.VOYAGE_FILE, "a", newline = " ") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Reykjavík", departure_time, arriving_abroad, arrival_time, 
            "Reykjavík", departure_time_home, arrival_time_home, plane_insignia, 
            captain, co_pilot, fsm, fa1, fa2, flight_number])
