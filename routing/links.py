from functions_behaviours_traits.loci import Locus
from functions_behaviours_traits.math_functions import two_d_distance_calculator
from nodes import Node, TransitHub, FreightHub, Start, End


class Link:
    def __init__(self, a, b):
        self.start_node = a
        self.end_node = b


class StraightLink(Link):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.length = two_d_distance_calculator(self.start_node.loci, self.end_node.loci)

    def get_link_length(self):
        return self.length

