from seasons import Birthdate
import pytest


def main():
    test_age_in_minutes()
    test_setter()
    test_str()


def test_age_in_minutes():
    birthdate = Birthdate("1900-01-01")
    birthdate2 = Birthdate("2020-01-01")
    birthdate3 = Birthdate("2022-01-01")
    assert (
        birthdate.age_in_minutes()
        == "Sixty-five million, five hundred ninety-four thousand, eight hundred eighty"
    )
    assert (
        birthdate2.age_in_minutes()
        == "Two million, four hundred eighty-one thousand, one hundred twenty"
    )
    assert (
        birthdate3.age_in_minutes()
        == "One million, four hundred twenty-eight thousand, four hundred eighty"
    )


def test_setter():
    with pytest.raises(SystemExit):
        Birthdate("cat")


def test_str():
    birthdate = Birthdate("1900-01-01")
    assert (
        str(birthdate)
        == "Sixty-five million, five hundred ninety-four thousand, eight hundred eighty minutes"
    )


if __name__ == "__main__":
    main()
