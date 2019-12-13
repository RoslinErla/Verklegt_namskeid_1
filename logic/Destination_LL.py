from model.DestinationM import Destination
from IO. destinationIO import DestinationIO
from datetime import datetime
import datetime
import string

class DestinationLL(Destination):

    def __init__(self):
        self.__destination = DestinationIO()
    
    def check_if_exists(self, check, num):
        destination_set = self.__destination.get_set(num)
        for elements in destination_set:
            if check == elements:
                return False
        else: 
            return True

    def validate_destination_num(self, destination_num):
        if len(destination_num) <=2:
            for letter in destination_num:
                if not letter.isdigit():
                    return False
            return True        
        return False
           

    def validate_destination_id(self, destination_id):  #  Check if id (KEF) only has alphabetical letters and is 3 letters long
        if len(destination_id) == 3: 
            for letter in destination_id:
                if not letter.isalpha():
                    return False
            return True
        return False

    
    def validate_destination_name(self, destination_name): #  Check if name only has alphabetical letters
        if type(destination_name) == str:
            for letter in destination_name:
                if not letter.isalpha():
                    return False
            return True
        return False
    
    def validate_country_name(self, country_name):  
        country_name = country_name.split()
        for elements in country_name:
            for letters in elements:
                if not letters.isalpha():
                    return False
        return True
    
    def validate_airport_name(self, airport_name):
        airport_name = airport_name.split()
        for elements in airport_name:
            for letters in elements:
                if not letters.isalpha():
                    return False
        return True
    
    def validate_flight_time(self, flight_time): # Eftir að búa til gögn fyrir þetta
        hours,minutes = flight_time.split()
        try:
            flight_time = datetime.datetime(int(hours),int(minutes))
            return True

        except ValueError:
            return False

    def validate_distance(self, distance): # Eftir að búa til gögn fyrir þetta, fjarlægð frá Íslandi, væntalega bara tölustafir
        for letter in distance:
            if not letter.isdigit():
                return False
        return True
    
    def validate_contact_name(self, contact_name): # Búið að búa til nöfnin, þurfa að vera bókstafir
        contact_name = contact_name.split()
        for elements in contact_name:
            for letter in contact_name:
                if not letter.isalpha():
                    return False
        return True
    
    def validate_contact_number(self, contact_number):
        for letter in contact_number:
            if not letter.isdigit():
                return False
        return True
    
    def validate_flight_number(self, flight_number):      
        """ Validates that the flight number is 6 letters long"""     # Mögulega að setja inn þá virkni að fyrstu 2 stafirnir þurfi að vera NA
        if len(flight_number) == 6:
            return True
        

    def create_destination(self,new_destination):
        destination_num, destination_name, destination_id, country, airport, flight_time, distance, emergency_contact, emergency_phone = new_destination.split(",")
        self.__destination.Add_destination_to_file(destination_num,destination_name,destination_id,country,airport,flight_time,distance,emergency_contact,emergency_phone)

    def change_destination(self, des, change, new):
        self.__destination.change_destination(des, change, new)













