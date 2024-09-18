from jar import Jar
import pytest

def test_init():
    assert Jar().capacity == 12
    with pytest.raises(ValueError):
        Jar(-1)
    assert Jar().size == 0

def test_str():
    assert str(Jar()) == ""
    j = Jar()
    j.deposit(3)
    assert str(j) == "🍪🍪🍪"

def test_deposit():
    with pytest.raises(ValueError):
        Jar().deposit(13)
    j = Jar()
    j.deposit(2)
    assert j.size == 2
    with pytest.raises(ValueError):
        j.deposit(12)

def test_withdraw():
    with pytest.raises(ValueError):
        Jar().withdraw(13)
    j = Jar()
    j.deposit(3)
    j.withdraw(2)
    assert j.size == 1
