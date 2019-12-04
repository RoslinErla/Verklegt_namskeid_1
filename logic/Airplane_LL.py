from model.AirplaneM import Airplane
import string

class Airplane_LL(Airplane):
    def __init__(self, inp):
        self.inp = inp
    
plane_type, type_ID, plane_insignia, model

    def validate_info(self):
        if type(self.inp) == str:
            for word in self.inp:
                for letter in word:
                    if letter.isalpha:
                        next
                    elif letter == "-":
                        next
                    else:
                        print("Oopsie")
                        break

