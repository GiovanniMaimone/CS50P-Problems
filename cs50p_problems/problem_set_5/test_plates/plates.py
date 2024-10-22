def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    # Start with at least two letters
    # No periods, spaces, or punctuation marks are allowed
    # Maximum of 6 characters and a minimum of 2 characters
    if 6 >= len(plate) >= 2 and plate[0:2].isalpha() and plate.isalnum():
        for char in plate:
            if char.isdigit():
                index = plate.index(char)
                if plate[index:].isdigit() and char != "0":
                    return True
                else:
                    return False

        return True
    return False


if __name__ == "__main__":
    main()
