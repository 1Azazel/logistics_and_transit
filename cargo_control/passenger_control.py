

class Passenger:
    def __init__(self, current_loci, destination, luggage):
        self.current_location = current_loci
        self.destination = destination
        self.luggage = luggage

    def add_luggage(self, new_luggage):
        self.luggage.append(new_luggage)


class Luggage:
    def __init__(self, size, weight):
        self.size = size
        self.weight = weight

