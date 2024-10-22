def main():
    fuel = input("Fraction: ")
    percentage = convert(fuel)
    print(gauge(percentage))


def convert(fuel):
    while True:
        x, y = fuel.split("/")
        try:

            int_x = int(x)
            int_y = int(y)

            if int_x > int_y and int_y != 0:
                fuel = input("Fraction: ")
                pass
            else:
                percentage = int((int_x / int_y) * 100)
                return int(percentage)

        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
