from Airplane_Modelclass import Airplane
class AirplaneLL(Airplane):
    def __init__(self, inp):
        self.inp = inp
    

    def validate_info(self):
        if type(self.inp) == str:
            for word in self.inp:
                try:
                    assert word != ""
                    assert word != "0"
                    assert word != "1"
                    assert word != "2"
                    assert word != "3"
                    assert word != "4"
                    assert word != "5"
                    assert word != "6"
                    assert word != "7"
                    assert word != "8"
                    assert word != "9"
                    assert word != "."
                    assert word != ","
                    # assert word != "" " ""
                    # assert word != "" ' ""
                    assert word != "#"
                    assert word != "$"
                    assert word != "%"
                    assert word != "&"
                    assert word != "/"
                    assert word != "("
                    assert word != ")"
                    assert word != "="
                    assert word != "@"
                    assert word != "€"
                    assert word != "{"
                    assert word != "}"
                    assert word != "["
                    assert word != "]"
                    assert word != "_"
                    assert word != "+"
                    assert word != "*"
                    assert word != "?"
                    assert word != "'"
                    assert word != "~"
                    assert word != "´"
                    assert word != "^"
                    assert word != ">"
                    assert word != "<"
                    assert word != "|"
                except:
                    print("Oopsie")
                    break


alpha = AirplaneLL("10")
alpha.validate_info()