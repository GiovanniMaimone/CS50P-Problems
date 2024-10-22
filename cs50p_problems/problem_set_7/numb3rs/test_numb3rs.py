from numb3rs import validate


def main():
    test_values()
    test_range()

def test_values():
    assert validate(r"127.0.0.1") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.512.512.512") == False
    assert validate(r"cat") == False

def test_range():
    assert validate(r"300.1.1.1") == False
    assert validate(r"1.300.1.1") == False
    assert validate(r"1.1.300.1") == False
    assert validate(r"1.1.1.300") == False


if __name__ == "__main__":
    main()
