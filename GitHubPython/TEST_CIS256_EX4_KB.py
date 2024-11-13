# CIS256
# Keynner Blas
# Fall 2024
# EX4 - Pytest

import pytest

# From py file we will import function that will be tested
from CIS256_EX4_KB import select_random_animal, check_vowel_in_word

# Function will test that random animal selected is in list predefined
def test_select_random_animal():
    animal = select_random_animal()
    assert animal in [
        "ALLIGATOR", "ALPACA", "ANACONDA", "ANT", "ARMADILLO", 
        "ELEPHANT", "EAGLE", "EEL", "ELK", "IMPALA", "IBIS",
        "IGUANA", "IBEX", "INDRI", "OTTER", "OCTOPUS", "ORANGUTAN", 
        "ORCA", "OWL", "OYSTER", "OSTRICH", "ORIOLE", "UTONAGAN", "UNAU", 
        "URUTU", "UMBRELLABIRD", "URCHIN"
    ]

