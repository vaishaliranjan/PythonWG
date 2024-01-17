# Delhi -> Guwahati-> Lakhimpur
from typing import List
class Flight:
    def __init__(self, segments):
        self.segments=segments

    @property
    def departure_point(self)-> str:
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self,val):
        self.segments[0].departure=val


class Segment:
    def __init__(self, departure, destination):
        self.departure=departure
        self.destination=destination

flight= Flight([Segment('GLA','LHR')])
print(flight.departure_point)
flight.segments[0].departure='EDI'
flight.departure_point="DEL"
print(flight.departure_point)

#flight.departure_point=EDI
