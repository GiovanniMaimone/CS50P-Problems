def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    lowercase_greeting = greeting.lower().strip()
    value = int()

    if "hello" in lowercase_greeting:
        value += 0

    elif "h" == lowercase_greeting[0]:
        value += 20

    else:
        value += 100

    return value


if __name__ == "__main__":
    main()
