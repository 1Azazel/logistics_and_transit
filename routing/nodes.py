from functions_behaviours_traits.loci import Locus


class Node:
    def __init__(self, name):
        self.name = name
        self.loci = Locus()

    def set_position(self, x, y, z):
        self.loci.add_xyz_values(x, y, z)


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
