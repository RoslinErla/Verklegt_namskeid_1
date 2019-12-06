from model.DestinationM import Destination

import string

class DestinationLL(Destination):

    def __init__(self):
        pass
        

    def add_employee(self):
        pass

    def change_employee(self):
        pass

    def validate_destination_id(self, destination_id):  #  Check if id (KEF) only has alphabetical letters and is 3 letters long
        if len(destination_id) == 3: 
            for letter in destination_id:
                if letter.isalpha():
                    return True
        else:
            return False
        return True
    
    def validate_destination_name(self, destination_name): #  Check if name only has alphabetical letters
        for letter in destination_name:
            if letter.isalpha():
                return True
    

    def validate_country_name(self, country_name):  # Eftir að búa til gögn fyrir þetta, geri ráð fyrir að það séu bara bókstafir
        for letter in country_name:
            if letter.isalpha():
                return True
    
    def validate_airport_name(self, airport_name): # Eftir að búa til gögn fyrir þetta, geri ráð fyrir að það séu bara bókstafir
        for letter in airport_name:
            if letter.isalpha():
                return True
    
    def validate_flight_time(self, flight_time): # Eftir að búa til gögn fyrir þetta
        # Ekki viss hvernig hann ætti að vera .. 
        pass

    def validate_distance(self, distance): # Eftir að búa til gögn fyrir þetta, fjarlægð frá Íslandi, væntalega bara tölustafir
        for letter in distance:
            if letter.isdigit():
                return True
    
    def validate_contact_name(self, contact_name): # Búið að búa til nöfnin, þurfa að vera bókstafir
        for letter in contact_name:
            if letter.isalpha():
                return True
    
    def validate_contact_number(self, contact_number):
        for letter in contact_number:
            if letter.isdigit() or letter != "-":
                return True
       











