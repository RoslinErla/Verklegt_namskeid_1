from flight import Flight

class Voyage(Flight):
    def __init__(self, employee, flight_out, flight_home):
        self.employee = employee
        self.flight_out = flight_out   # useless ?
        self.flight_home = flight_home  # useless ? 
    

    def __str__(self):
        pass


