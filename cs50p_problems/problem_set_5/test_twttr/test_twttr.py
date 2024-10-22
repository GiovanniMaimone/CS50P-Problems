from twttr import shorten

def test_vowels():
    assert shorten("giovanni") == "gvnn"
    assert shorten("amazon") == "mzn"
    assert shorten("aeiou") == ""

def test_upper_lower_case():
    assert shorten("giovanni") == "gvnn"
    assert shorten("GIOVANNI") == "GVNN"
    assert shorten("Giovanni") == "Gvnn"

def test_numbers():
    assert shorten("12345") == "12345"
    assert shorten("9876") == "9876"

def test_punctuation():
    assert shorten("!@#$") == "!@#$"
    assert shorten("*&¨%") == "*&¨%"
