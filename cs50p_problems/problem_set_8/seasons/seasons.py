from datetime import date, datetime
import sys
import inflect


class Birthdate:
    def __init__(self, birthdate):
        self.birthdate = birthdate
        self.p = inflect.engine()

    @property
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate):
        try:
            self._birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()

        except ValueError:
            sys.exit("Invalid date")

    def age_in_minutes(self):
        today = date.today()
        delta_age = today - self.birthdate
        age_minutes = delta_age.days * 24 * 60
        return self.p.number_to_words(age_minutes, andword="").capitalize()

    @classmethod
    def get_birthdate(cls):
        birthdate = input("Date of Birth: ")
        return cls(birthdate)

    def __str__(self):
        return f"{self.age_in_minutes()} minutes"


def main():
    birthdate = Birthdate.get_birthdate()
    print(birthdate)


if __name__ == "__main__":
    main()
