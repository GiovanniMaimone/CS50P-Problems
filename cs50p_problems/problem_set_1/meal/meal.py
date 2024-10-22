def main():
    present_time = input("what time is it?: ")
    time = convert(present_time)

    if 7 <= time and 8 >= time:
        print("breakfast time")

    elif 12 <= time and 13 >= time:
        print("lunch time")

    elif 18 <= time and 19 >= time:
        print("dinner time")

def convert(time):
    hours,minutes = time.split(":")
    float_minutes = float(minutes) / 60
    float_hours = float(hours)
    return float_minutes + float_hours

if __name__ == "__main__":
    main()
