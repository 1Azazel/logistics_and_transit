import math

num_of_decimals = 2


def distance_calculator(a, b):
    x = a.x - b.x
    y = a.y - b.y
    sum_of_squares = (x ** 2) + (y ** 2)
    result = round(math.sqrt(sum_of_squares), num_of_decimals)
    distance = abs(result)
