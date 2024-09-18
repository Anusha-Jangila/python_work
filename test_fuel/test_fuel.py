from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert("c/1")
    with pytest.raises(ValueError):
        convert("1/c")
    with pytest.raises(ValueError):
        convert("a/c")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("3/2")
    assert convert("2/3") == 67

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(98) == "98%"