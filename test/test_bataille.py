import pytest
from bataille import *
from utils import *

def test_table_1():
    to_be_tested = [
        # pole_angle, latitude, result
        (24, 15, 0.24),
        (47, 30, 0.34),
        (74, 54, 0.22),
        (85, 52, 0.07),
    ]
    
    for row in to_be_tested:
        result = table_1(row[0], row[1])
        assert round_float(result,2) == row[2]

def test_table_2():
    to_be_tested = [
        # declinaison, latitude, result
        (7, 33, 0.10),
        (26, 53, 0.29),
        (54, 85, 0.12),
        (83, 16, 7.83),
    ]
    
    for row in to_be_tested:
        result = table_2(row[0], row[1])
        assert round_float(result,2) == row[2]