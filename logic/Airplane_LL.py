from IO.airplaneIO import AirplaneIO
from model.AirplaneM import Airplane
import string

class AirplaneLL(Airplane):
    def __init__(self):
        self.__airplaneio = AirplaneIO()

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
        return self.__airplaneio.check_if_available(date)

    def check_if_in_available(self,date,plane_insignia):
        a = self.check_if_available(date)
        for elements in a:
            if elements[2] == plane_insignia:
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
        
    # def change_plane(self, planeinsignia, change, new):
    #     self.__airplaneio.change_airplane(planeinsignia, change, new)
