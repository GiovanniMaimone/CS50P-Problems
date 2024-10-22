from working import convert
import pytest


def main():
    test_ValueError()
    test_convert()


def test_ValueError():
    with pytest.raises(ValueError):
        convert(r"9:60 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert(r"9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert(r"09:00 AM - 17:00 PM")


def test_convert():
    assert convert(r"9 AM to 5 PM") == "09:00 to 17:00"
    assert convert(r"9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert(r"10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert(r"10:30 PM to 8 AM") == "22:30 to 08:00"


if __name__ == "__main__":
    main()