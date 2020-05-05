import math

from utils import *

def table_1(pole_angle, latitude):
    return math.cos(math.radians(pole_angle))*math.sin(math.radians(latitude))

def table_2(declinaison, latitude):
    return math.tan(math.radians(declinaison))*math.cos(math.radians(latitude))