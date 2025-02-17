import pytest
from main import prueba, mayor_que

def test_prueba():
    assert prueba(2,5)==7

@pytest.mark.parametrize(
    [
        (5,1,6),
        (6, sum(4,2),12)
        
    ]
)

def test_mayorque():
    assert mayor_que(20,19)