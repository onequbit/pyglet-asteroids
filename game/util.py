# force python 3.* compability
from __future__ import absolute_import, division, print_function

# regular imports below:
import math
from builtins import bytes, input, int, object, open, pow, range, round, str, super, zip
from random import uniform


def distance(point_1=(0, 0), point_2=(0, 0)):
    return math.sqrt( (point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

def random_coordinates(x_range, y_range):
    return uniform(-x_range/2, x_range/2), uniform(-y_range/2, y_range/2)

def random_rotation():
    return uniform(0.0, 360.0)

def random_velocity_2d(x_range, y_range):
    return uniform(*x_range), uniform(*y_range)