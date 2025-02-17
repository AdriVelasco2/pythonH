import pytest
from pytesting.main import prueba, mayor_que

def test_prueba():
    assert prueba(2,5)==7

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (5,1,6),
        (6, sum([4,2]),12)   
    ]
)
def test_mayorque(input_x, input_y, expected):
    assert mayor_que(20,19)