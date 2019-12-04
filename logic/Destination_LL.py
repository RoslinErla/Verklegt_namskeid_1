from model.DestinationM import Destination

class DestinationLL(Destination):

    def __init__(self, inp):
        # self.__IOAPI = IOAPI()
        self.inp = inp
        

    def add_employee(self):
        pass

    def change_employee(self):
        pass

    def validate_destination_id(self, destination_id):  #  Check if id (KEF) only has alphabetical letters and is 3 letters long
        if type(destination_id) == str:
            for word in destination_id:
                for letter in word:
                    if letter.isalpha and len(self.inp) == 3:
                        return True
    
    def validate_destination_name(self, destination_name): #  Check if name only has alphabetical letters
        if type(destination_name) == str:
            for word in destination_name:
                for letter in word:
                    if letter.isalpha:
                        return True


