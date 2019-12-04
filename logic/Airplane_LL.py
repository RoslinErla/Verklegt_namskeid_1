<<<<<<< HEAD
from model.AirplaneM import Airplane
=======
<<<<<<< HEAD
from model.AirplaneM import Airplane
=======
from ..model.AirplaneM import Airplane
>>>>>>> 1b6134f8a2205e33bf5c50a5f46c6b3d6915d04e
>>>>>>> cbbf69df3ba771b343571cd31bd41b04559c40cf
import string

class Airplane_LL(Airplane):
    def __init__(self, inp):
        self.inp = inp
    
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

