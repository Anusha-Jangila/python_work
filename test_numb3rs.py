from numb3rs import validate

def test_pattern():
    assert validate("a.0.2.1") == False
    assert validate(".0.2.1") == False
    assert validate("10.2.1") == False
    assert validate("3.c.2.1") == False
    assert validate("3..2.1") == False
    assert validate("3.4.d.1") == False
    assert validate("3.4..1") == False
    assert validate("3.4.1.") == False
    assert validate("3.4.1.e") == False
    assert validate("3.4.1.5") == True

def test_value():
    assert validate("123.43.23.1") == True
    assert validate("256.43.23.1") == False
    assert validate("25.432.23.1") == False
    assert validate("25.42.2390.1") == False
    assert validate("25.42.239.1000") == False
