from routing_functions import distance_calculator


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


class Load:
    def __init__(self, name, quantity, weight, destination):
        self.name = name
        self.quantity = quantity
        self.weight = weight
        self.destination = destination


class Loci:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, loci):
        self.loci = loci


class TransitHub(Node):
    def __init__(self, loci):
        super().__init__(loci)
        self.departures = []
        self.arrivals = []

    def add_arrivals(self, arrival_list):
        self.arrivals.append(arrival_list)

    def add_departures(self, departure_list):
        self.departures.append(departure_list)

    def get_arrivals(self):
        return self.arrivals

    def get_departures(self):
        return self.departures

    def load_passenger(self, passenger_car, passenger_list=0):
        for i in self.departures:
            passenger_car.occupants.append(self.departures[i])
            del self.departures[i]
        return passenger_car

    def unload_passenger(self, passenger_car, passenger_list=0):
        for i in self.arrivals:
            self.arrivals.append(passenger_car.occupants[i])
            del passenger_car.occupants[i]
            return passenger_car


class FreightHub(Node):
    def __init__(self, loci):
        super().__init__(loci)
        self.incoming_load_list = []
        self.outgoing_load_list = []
        self.node_storage = []

    def add_incoming_load_list(self, load_list):
        self.incoming_load_list.append(load_list)

    def add_outgoing_load_list(self, load_list):
        self.outgoing_load_list.append(load_list)

    def load_freight_car(self, freight_car, load_list=0):
        for i in self.node_storage:
            freight_car.hold.append(self.node_storage[i])
            del self.node_storage[i]
        return freight_car

    def unload_freight_car(self, freight_car, load_list=0):
        for i in freight_car.hold:
            self.node_storage.append(freight_car.hold[i])
            del freight_car.hold[i]
        return freight_car


class Start(Node):
    def __init__(self, loci):
        super().__init__(loci)


class End(Node):
    def __init__(self, loci):
        super().__init__(loci)


class Link:
    def __init__(self, a, b, length=0):
        self.node_1 = a
        self.node_2 = b
        self.length = distance_calculator(self.node_1.loci, self.node_2.loci)

    def get_link_length(self):
        return self.length


# A route is composed of an ordered list of Node and Links
class Route:
    def __init__(self, start, end):
        self.start = start
        self.end = end
