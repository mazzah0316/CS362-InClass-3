import pytest
import calc



def test_addition():
    assert calc.add(1, 2) == 3

def test_subtraction():
    assert calc.sub(1,2) == -1

def test_muliplication():
    assert calc.mult(1,2) == 2

def test_division():
    assert calc.div(1,2) == 0.5