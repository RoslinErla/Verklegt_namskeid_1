from model.destinationM import destination
import csv

class DestinationIO:
    DESTINATION_FILE = "./files/destination.csv"

    def __init__(self):
        pass

    def load_destination_from_file_alphabetically(self):
        pass

    def Add_destination_to_file(self):
        with open(self.DESTINATION_FILE, "a", newline = " ") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([])
