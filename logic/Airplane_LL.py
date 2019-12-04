from model.AirplaneM import Airplane
import string

class AirplaneLL(Airplane):
    def __init__(self, inp):
        self.inp = inp

    def strip_split(self):
        split_stripped = self.inp.strip().split(", ")
        validate_manufacturer(split_stripped[0])
        validate_typeID(split_stripped[1])
        validate_plane_insignia(split_stripped[2])      
        model(split_stripped[3])

    def validate_manufacturer(self):
        if type(self.inp) == str:
            for letter in self.inp:
                if letter.isalpha == False:
                        return False
        return True

    def validate_typeID(self):
        if type(self.inp) == str:
            for letter in self.inp:
                if letter.isalpha == False and letter.isdigit == False:
                    return False
        return True

    def validate_plane_insignia(self):
        if type(self.inp) == str:
            if self.inp[0:3] != "TF-":
                return False
            if len(self.inp) != 6:
                return False
            for num, letter in enumerate(self.inp):
                if letter != "-" and num == 2:
                    return False
                if letter.isalpha() == False:
                    return False                
        return True

    def validate_model(self):
        if type(self.inp) == str:
            for letter in self.inp:
                if letter.isalpha == False and letter.isdigit == False:
                    return False
        return True

    # def create_plane(self, ):

    # def change_plane(self, ):
