class Destination():
    def __init__(self, destination_name, destination_id, country, airport, flight_time, distance, contact_name, contact_phone_number):
        self.__destination_id = destination_id
        self.__destination_name = destination_name
        self.__country = country
        self.__airport = airport
        self.__flight_time = flight_time
        self.__distance = distance
        self.__contact_name = contact_name
        self.__contact_phone_number = contact_phone_number

    def __str__(self):
        return "{},{},{},{},{},{},{},{}".format(self.__destination_id, self.__destination_name, self.__county, self.__airport,
        self.__flight_time, self.__distance, self.__contact_name, self.__contact_phone_number)

    def get_destinantion_id(self):
        return self.__destination_id

    def get_destination_name(self):
        return self.__destination_name
    
    def get_country(self, country):
        return self.__country
    
    def get_airport(self, airport):
        return self.__airport
    
    def get_flight_time(self, flight_time):
        return self.__flight_time
    
    def get_distance(self, distance):
        return self.__distance
    
    def get_contact_name(self, contact_name):
        return self.__contact_name
    
    def get_contact_phone_number(self, contact_phone_number):
        return self.__contact_phone_number
    