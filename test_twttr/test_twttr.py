from twttr import shorten

def test_uppercase():
    assert shorten("ANUSHA") == "NSH"
    assert shorten("EGG") == "GG"
    assert shorten("ONION") == "NN"

def test_lowercase():
    assert shorten("anusha") == "nsh"
    assert shorten("egg") == "gg"
    assert shorten("onion") == "nn"

def test_numbers():
    assert shorten("AJ123") == "J123"

def test_punctuation():
    assert shorten("myAJ1!") == "myJ1!"