from plates import is_valid

def test_special_chars():
    assert is_valid("anu.22") == False
    assert is_valid("anu 22") == False
    assert is_valid("anu!22") == False
    assert is_valid("AAAA22") == True

def test_starts_with_2letters():
    assert is_valid("AA1234") == True
    assert is_valid("1A1234") == False
    assert is_valid("121234") == False
    assert is_valid("A11234") == False
    assert is_valid("12ABCD") == False

def test_length():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ANCD345") == False

def test_format():
    assert is_valid("AB34CD") == False
    assert is_valid("ABCD34") == True
    assert is_valid("ABCD01") == False