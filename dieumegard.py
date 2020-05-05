import math

from utils import *

def table_1(degres, minutes):
    return -math.log10(1-math.cos(math.radians(deg_min_to_deg_dec(degres, minutes))))

def table_2(degres, minutes):
    return -math.log10(math.cos(math.radians(deg_min_to_deg_dec(degres, minutes))))

def table_3(thousand_and_hundreds, tens_and_units):
    value = thousand_and_hundreds/100+tens_and_units/10000
    return -math.log10(value)

def table_A(degres, minutes):
    return 1-math.cos(math.radians(deg_min_to_deg_dec(degres, minutes)))