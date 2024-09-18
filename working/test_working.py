from working import convert
import pytest

def test_format1(): #9 AM to 5 PM
    with pytest.raises(ValueError):
        convert("0 AM to 1 PM")
    assert convert("1 AM to 2 PM") == "01:00 to 14:00"
    assert convert("10 AM to 11 PM") == "10:00 to 23:00"
    with pytest.raises(ValueError):
        convert("13 AM to 1 PM")
    with pytest.raises(ValueError):
        convert("1 AM to 14 PM")

def test_format2(): #9:00 AM to 5:00 PM
    with pytest.raises(ValueError):
        convert("1:00 AM to 0:00 PM")
    assert convert("3:02 AM to 4:07 PM") == "03:02 to 16:07"
    assert convert("11:00 AM to 10:00 PM") == "11:00 to 22:00"
    with pytest.raises(ValueError):
        convert("1:00 AM to 14:00 PM")
    with pytest.raises(ValueError):
        convert("1:60 AM to 4:00 PM")

def test_meridian():
    assert convert("2 AM to 3 PM") == "02:00 to 15:00"
    assert convert("1 PM to 2 AM") == "13:00 to 02:00"

def test_empty_string():
    with pytest.raises(ValueError):
        convert(" to ")
    with pytest.raises(ValueError):
        convert("to")