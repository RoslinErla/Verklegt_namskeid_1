class Flight():
    def __init__(self, departing_from, departure_time, arriving_at, arrival_time, aircraft_ID, captain, co_pilot, fsm, fa1, fa2):
        self.departing_from = departing_from
        self.departure_time = departure_time
        self.arriving_at = arriving_at
        self.arrival_time = arrival_time
        self.aircraft_ID = aircraft_ID
        self.captain = captain
        self.co_pilot = co_pilot
        self.fsm = fsm
        self.fa1 = fa1
        self.fa2 = fa2

    def __str__(self):
        pass
