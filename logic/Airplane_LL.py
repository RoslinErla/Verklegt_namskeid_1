from model.AirplaneM import Airplane
import string

class Airplane_LL(Airplane):
    def __init__(self, inp):
        self.inp = inp

    # def make_inp_dict(self):
    #     inp_dict = {}
    #     split_stripped = self.inp.strip().split(", ")
    #     inp_dict(split_stripped[0]) = validate_manufacturer(split_stripped[0])
    #     inp_dict(split_stripped[1]) = validate_typeID(split_stripped[1])
    #     inp_dict(split_stripped[2]) = validate_plane_insignia(split_stripped[2])      
    #     inp_dict(split_stripped[3]) = model(split_stripped[3])

    def validate_manufacturer(self):
        if type(self.inp) == str:
            for word in self.inp:
                for letter in word:
                    if letter.isalpha:
                        return True

    def validate_typeID(self):
        if type(self.inp) == str:
            for word in self.inp:
                for letter in word:
                    if letter.isalpha or letter.isdigit:
                        return True

    def validate_plane_insignia(self):
        if type(self.inp) == str:
            for word in self.inp:
                if word != "TF-":
                    for letter in word:
                        if letter.isalpha:
                            return True

    def validate_model(self):
        if type(typeID) == str:
            for word in self.inp:
                for letter in word:
                    if letter.isalpha or letter.isdigit:
                        return True

    # def create_plane(self, ):

    # def change_plane(self, ):
