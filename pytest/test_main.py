import pytest
from main import prueba, mayor_que

def test_prueba():
    assert prueba(2,5)==7

@pytest.mark.parametrize(
    [
        (5,1),
        (6, 7)
        
    ]
)

def test_mayorque():
    assert mayor_que(20,19)