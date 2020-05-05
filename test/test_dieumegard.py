import pytest
from dieumegard import *
from utils import *

def test_table_1():
    to_be_tested = [
        # deg, min, result
        (270, 0, 0.),
        (278, 34, 0.0701),
        (326, 59, 0.7919),
        # (0, 4, 6.1693) # pas conforme aux tables de navastro
        (5, 15, 2.3773),
    ]
    
    for row in to_be_tested:
        result = table_1(row[0], row[1])
        assert round_float(result,4) == row[2]

def test_table_2():
    to_be_tested = [
        # deg, min, result
        (4, 0, 0.0011),
        (38, 20, 0.1055),
        (66, 45, 0.4037),
        (53, 60, 0.2308),
    ]
    
    for row in to_be_tested:
        result = table_2(row[0], row[1])
        assert round_float(result,4) == row[2]

def test_table_3():
    to_be_tested = [
        # milles et centaines, dizaines et unités, result
        (6, 30, 1.2007),
        (21, 70, 0.6635),
        (48, 30, 0.3161),
        (76, 8, 0.1187),
    ]
    
    for row in to_be_tested:
        result = table_3(row[0], row[1])
        assert round_float(result,4) == row[2]

def test_table_A():
    to_be_tested = [
        # deg, min, result
        (4, 5, 0.0025),
        (23, 20, 0.0818),
        (56, 45, 0.4517),
        (88, 55, 0.9811),
    ]
    
    for row in to_be_tested:
        result = table_A(row[0], row[1])
        assert round_float(result,4) == row[2]