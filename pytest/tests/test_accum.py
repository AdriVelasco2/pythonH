import pytest
from stuff.accum import Accumulator

def test_accumulator_init():
    accum = Accumulator()
    assert accum.count==0
    
def test_accumulator_one():
    accum= Accumulator()
    accum.add()
    assert accum.count ==1
    
def test_accumulator_two():
    accum= Accumulator
    accum.add(3)
    assert accum.count==3
    