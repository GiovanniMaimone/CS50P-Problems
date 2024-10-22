import inflect

correct = inflect.engine()
namelist = []

while True:
    try:
        name = input("Name: ")
        namelist.append(name)

    except EOFError:
        correctnames = correct.join(namelist)
        print(f"Adieu, adieu, to {correctnames}")
        break


