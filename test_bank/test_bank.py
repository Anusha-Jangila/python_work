from bank import value

def test_lowercase():
    assert value("hello") == 0
    assert value("howdy") == 20
    assert value("what's up") == 100

def test_uppercase():
    assert value("HELLO") == 0
    assert value("HOWDY") == 20
    assert value("What's up") == 100

def test_numbers():
    assert value("123") == 100

def test_punctuation():
    assert value("!") == 100

def test_leading_spaces():
    assert value(" HELLO") == 0
    assert value("  HOWDY") == 20
    assert value("   What's up") == 100

def test_whitespace():
    assert value("    ") == 100