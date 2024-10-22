import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if times := re.search(
        r"^([0-9]{1,2}):?([0-9]{0,2})? (AM|PM) to ([0-9]{1,2}):?([0-9]{0,2})? (PM|AM)$",
        s,
        re.IGNORECASE,
    ):
        # Variables
        first_hour = int(times.group(1))
        first_min = times.group(2) if times.group(2) else "00"
        second_hour = int(times.group(4))
        second_min = times.group(5) if times.group(5) else "00"

        # ValueError cases
        if int(first_min) >= 60 or int(second_min) >= 60:
            raise ValueError

        # Convert first hour
        right_hour1 = int(first_hour)
        if times.group(3) == "PM" and first_hour != 12:
            right_hour1 += 12
        elif times.group(3) == "AM" and first_hour == 12:
            right_hour1 = 0

        time1 = f"{right_hour1:02}:{first_min}"

        # Convert second hour
        right_hour2 = int(second_hour)
        if times.group(6) == "PM" and second_hour != 12:
            right_hour2 += 12
        elif times.group(6) == "AM" and second_hour == 12:
            right_hour2 = 0

        time2 = f"{right_hour2:02}:{second_min}"

        # Right string
        right_time = f"{time1} to {time2}"
        return right_time

    else:
        raise ValueError


if __name__ == "__main__":
    main()
