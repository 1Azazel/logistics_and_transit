import math
from loci import Locus

num_of_decimals = 3


def two_d_distance_calculator(a, b):
    x = a.x - b.x
    y = a.y - b.y
    sum_of_squares = (x ** 2) + (y ** 2)
    result = round(math.sqrt(sum_of_squares), num_of_decimals)
    distance = abs(result)
    return distance


def three_d_distance_calculator(a, b):
    x = a.x - b.x
    y = a.y - b.y
    z = a.z - b.z
    sum_of_squares = (x ** 2) + (y ** 2) + (z ** 2)
    result = round(math.sqrt(sum_of_squares), num_of_decimals)
    distance = abs(result)
    return distance


def find_midpoint(a, b):
    c = Locus()
    cx = (a.x + b.x) / 2
    cy = (a.y + b.y) / 2
    cz = (a.z + b.z) / 2
    c.add_xyz_values(cx, cy, cz)
    return c
