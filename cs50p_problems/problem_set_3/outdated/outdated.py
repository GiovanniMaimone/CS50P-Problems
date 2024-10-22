months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    date = input("Date: ").title().strip()
    try:
        month, day, year = date.split("/")
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            break

    except:
        try:
            month_space, day_space, year = date.split(" ")
            day = day_space.replace(",", " ")
            for i in range(len(months)):
                if month_space == months[i]:
                    month = i + 1
            if not day_space.endswith(","):
                continue

            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                break
        except:
            pass
print(f"{year}-{int(month):02}-{int(day):02}")
