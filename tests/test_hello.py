from hello import hello

def test_argument():
    assert hello("David") == "Hello, David!"

def test_default():
    assert hello() == "Hello, World!"