from model.AirplaneM import Airplane
import string

class Airplane_LL(Airplane):
    def __init__(self, inp):
        self.inp = inp

    

    def strip_split_inp(self):
        split_stripped = self.inp.strip().split(", ")


    def validate_manufacturer(self, manufacturer):
        if type(manufacturer) == str:
            for word in manufacturer:
                for letter in word:
                    if letter.isalpha:
                        return True

    def validate_typeID(self, typeID):
        if type(typeID) == str:
            for word in typeID:
                for letter in word:
                    if letter.isalpha or letter.isdigit:
                        return True

    def validate_plane_insignia(self, plane_insignia):
        if type(plane_insignia) == str:
            for word in plane_insignia:
                for letter in word:
                    if letter.isalpha or letter == "-":
                        return True

    def validate_model(self, model):
        if type(typeID) == str:
            for word in model:
                for letter in word:
                    if letter.isalpha or letter.isdigit:
                        return True

