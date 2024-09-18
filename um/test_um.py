from um import count

def test_length():
    assert count("Um, ok um...") == 2
    assert count("Um, thanks for the album") == 1
    assert count("um") == 1

def test_case():
    assert count("UM") == 1
    assert count("um") == 1

def test_match():
    assert count("yummy") == 0
    assert count("Um?") == 1
    assert count("yum") == 0