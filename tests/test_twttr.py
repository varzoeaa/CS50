from twttr import twttr


def test_default():
    assert twttr("Twitter") == "Twttr"

def test_empty_string():
    assert twttr("") == ""

def test_no_vowels():
    assert twttr("Twttr") == "Twttr"

def test_all_vowels():
    assert twttr("aeiouAEIOU") == ""




