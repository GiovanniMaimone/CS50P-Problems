import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        for i in range(1, 5):
            if int(matches.group(i)) < 0 or int(matches.group(i)) > 255:
                return False
        return True

    else:
        return False


if __name__ == "__main__":
    main()
