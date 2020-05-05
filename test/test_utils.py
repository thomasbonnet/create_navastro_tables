import pytest

from utils import *


def test_deg_min_to_deg_dec():
    to_be_tested = [
        # deg, min, result
        (5, 30, 5.5),
        (56, 15, 56.25),
    ]
    for row in to_be_tested:
        assert deg_min_to_deg_dec(row[0], row[1]) == row[2]

def test_round_float():
    to_be_tested = [
        # float, min, result
        (1.0256545654, 4, 1.0257),
        (2.654123456, 1, 2.7),
    ]
    for row in to_be_tested:
        assert round_float(row[0], row[1]) == row[2]