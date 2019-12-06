from model.AirplaneM import Airplane
import string

class AirplaneLL(Airplane):
    def __init__(self):
        pass
    # def strip_split(self):
    #     """ Strips and splits "inp" and then runs each bit of that through the appropiet validate functions """
    #     split_stripped = self.__inp.strip().split(",")
    #     if validate_manufacturer(split_stripped[0]) == True and validate_typeID(split_stripped[1]) == True and validate_plane_insignia(split_stripped[2]) == True and model(split_stripped[3]) == True:
    #         return split_stripped

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

    def validate_model(self, model):
        """ validates whether "model" is a string and whether or not it's letters are numerals or in the alphabet. """
        if type(model) == str:
            for letter in model:
                if not letter.isalpha() and not letter.isdigit():
                    return False
            return True
        return False

    def create_plane(self, new_plane):
        pass
        
    def change_plane(self, change_plane):
        pass