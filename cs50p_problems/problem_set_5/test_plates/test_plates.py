from plates import is_valid

def test_alpha():
    assert is_valid("AA") == True
    assert is_valid("22AA") == False
    assert is_valid("22") == False

def test_length():
    assert is_valid("A") == False
    assert is_valid("AAA2222") == False

def test_number():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_zero():
    assert is_valid("AA02") == False
    assert is_valid("AA20") == True

def test_alpha_nume():
    assert is_valid("AA.22") == False

