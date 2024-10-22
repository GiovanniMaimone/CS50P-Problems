import sys
import csv
from tabulate import tabulate

try:

    if len(sys.argv) == 2:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            print(tabulate(reader, headers="keys", tablefmt="grid"))

    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

except FileNotFoundError:
    sys.exit("File does not exist")
