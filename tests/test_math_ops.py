from src.math_ops import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1,1) == 0

def test_subtract():
    assert subtract(5, 4) == 1
    assert subtract(3, 3) == 0