from model.AirplaneM import Airplane
import string

class AirplaneLL(Airplane):
    def __init__(self, inp):
        self.__inp = inp

    # def strip_split(self):
    #     """ Strips and splits "inp" and then runs each bit of that through the appropiet validate functions """
    #     split_stripped = self.__inp.strip().split(",")
    #     if validate_manufacturer(split_stripped[0]) == True and validate_typeID(split_stripped[1]) == True and validate_plane_insignia(split_stripped[2]) == True and model(split_stripped[3]) == True:
    #         return split_stripped

    def validate_manufacturer(self):
        """ Validates whether "self" """
        if type(self.__inp) == str:
            for letter in self.__inp:
                if not letter.isalpha:
                        return False
            return True
        return False

    def validate_typeID(self):
        if type(self.__inp) == str:
            for letter in self.__inp:
                if not letter.isalpha and not letter.isdigit:
                    return False
            return True
        return False

    def validate_plane_insignia(self):
        if type(self.__inp) == str:
            if self.__inp[0:3] != "TF-" or len(self.__inp) != 6:
                return False
            for num, letter in enumerate(self.__inp):
                if not letter.isalpha() and (letter != "-" and num == 2):
                    return False
            return True
        return False

    def validate_model(self):
        if type(self.__inp) == str:
            for letter in self.__inp:
                if not letter.isalpha and not letter.isdigit:
                    return False
            return True
        return False

    def create_plane(self):
        plane_info = strip_split()
        
    def change_plane(self, ):
        plane_info = strip_split()