import sys
import csv

after = []
try:

    if len(sys.argv) == 3:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                after.append(
                    {"first": first.strip(), "last": last, "house": row["house"]}
                )

        with open(sys.argv[2], "w") as file2:
            writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in after:
                writer.writerow(
                    {"first": row["first"], "last": row["last"], "house": row["house"]}
                )

    elif len(sys.argv) == 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")
