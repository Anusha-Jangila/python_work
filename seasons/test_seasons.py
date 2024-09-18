from seasons import validate_dob

def test_validate_dob():
    assert validate_dob("1990-01-01") == True
    assert validate_dob("January 1, 1990") == False
    assert validate_dob("1990/01/01") == False
