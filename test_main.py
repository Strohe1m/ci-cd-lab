from main import add

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_fail():
    assert add(2, 2) == 5
