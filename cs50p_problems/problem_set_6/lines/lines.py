import sys

try:

    if len(sys.argv) == 2:
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
        with open(sys.argv[1]) as file:
            lines = 0
            for line in file:
                if not line.isspace():
                    if not line.lstrip().startswith("#"):
                        lines += 1
            print(lines)

    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

except FileNotFoundError:
    sys.exit("File does not exist")
