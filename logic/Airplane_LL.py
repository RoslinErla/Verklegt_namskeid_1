from IO.airplaneIO import AirplaneIO
from IO.employeeIO import EmployeeIO
from model.AirplaneM import Airplane
import string

class AirplaneLL(Airplane):
    def __init__(self):
        self.__airplaneio = AirplaneIO()
        self.__employeeio = EmployeeIO()

    def check_if_exists(self,check,num):
        destination_set = self.__airplaneio.get_set(num)
        for elements in destination_set:
            if check == elements:
                return True
        else: 
            return False

    def validate_manufacturer(self, manufacturer):
        """ Validates whether "manufacturer" is a string and whether or not every letter is a part of the alphabet. """
        if type(manufacturer) == str:
            for letter in manufacturer:
                if not letter.isalpha():
                    return False
            return True
        return False

    def validate_typeID(self, type_ID):
        """ validates whether "type_ID" is a string and if every letter is either a numeral or a part of the alphabet """
        if type(type_ID) == str:
            for letter in type_ID:
                if not letter.isalpha() and not letter.isdigit():
                    return False
            return True
        return False

    def validate_plane_insignia(self, plane_insignia):
        """ Validates whether "plane_insignia" is a string, if it has the right format and whether or not every letter, outside of "-" is a part of the alphabet """
        if type(plane_insignia) == str:
            if plane_insignia[0:3] != "TF-" or len(plane_insignia) != 6:
                return False
            for num, letter in enumerate(plane_insignia):
                if not letter.isalpha() and (letter != "-" and num == 2):
                    return False
            return True
        return False

    def check_if_available(self,date):
        self.__airplaneio.check_if_available(date)
        return str(self.__airplaneio)

    def check_if_matches(self,date):
        self.__airplaneio.check_if_available(date)
        return self.__airplaneio.get_airplane_list()

    def check_if_in_available(self,date,plane_insignia):
        a = self.check_if_matches(date)
        for airplane in a:
            if airplane.get_plane_insignia() == plane_insignia:
                return True
        return False

    def validate_model(self, model):
        """ validates whether "model" is a string and whether or not it's letters are numerals or in the alphabet. """
        if type(model) == str:
            for letter in model:
                if not letter.isalpha() and not letter.isdigit():
                    return False
            return True
        return False

    def create_plane(self, new_plane):
        manufacturer, type_id, plane_insignia, model = new_plane.split(",") 
        self.__airplaneio.Add_airplane_to_file(manufacturer, type_id, plane_insignia, model)
        
    def load_from_file(self):
        self.__airplaneio.load_airplane_from_file()
        return str(self.__airplaneio)

    def display_by_licence(self, type_id):
        self.__employeeio.display_by_licence(type_id)
        return str(self.__employeeio)    
