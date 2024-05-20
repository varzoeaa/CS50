from bank import value

def test_default():
    assert value("Hello") == "0$"
    assert value("Hi") == "20$"
    assert value("Bye") == "100$"

def test_corner():
    assert value("H") == "20$"

