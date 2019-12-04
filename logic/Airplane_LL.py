from AirplaneM import Airplane
import string

class AirplaneLL(Airplane):
    def __init__(self, inp):
        self.inp = inp
    

    def validate_info(self):
        if type(self.inp) == str:
            for word in self.inp:
                if word.isalpha == True:
                    next
                elif word == " - ":
                    next
                else:
                    print("Oopsie")
                    break


alpha = AirplaneLL("10")
alpha.validate_info()