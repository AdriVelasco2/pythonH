import pytest
import sys
sys.path.append('..')
from stuff.accum import Accumulator

@pytest.fixture
def accum():
  return Accumulator()

@pytest.fixture
def accum2():
  return Accumulator()

def test_accumulator_init(accum, accum2):
  assert accum.count == 0