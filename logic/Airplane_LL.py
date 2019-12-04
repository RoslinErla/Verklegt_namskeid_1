from model.AirplaneM import Airplane
import string

class AirplaneLL(Airplane):
    def __init__(self, inp):
        self.inp = inp

    def make_inp_dict(self):
        split_stripped = self.inp.strip().split(", ")
        validate_manufacturer(split_stripped[0])
        validate_typeID(split_stripped[1])
        validate_plane_insignia(split_stripped[2])      
        model(split_stripped[3])

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
            if self.inp[0:3] != "TF-":
                return False
            if len(self.inp) != 6:
                return False
            for num, letter in enumerate(self.inp):
                if letter != "-" and num == 2:
                    if letter.isalpha() == False:
                        return False                
        return True

    def validate_model(self):
        if type(typeID) == str:
            for word in self.inp:
                for letter in word:
                    if letter.isalpha or letter.isdigit:
                        return True

    # def create_plane(self, ):

    # def change_plane(self, ):
