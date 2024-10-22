answer = input("The Answer to the Great Question…: ")

match answer.lower().strip():
    case "42" | "forty-two" | "forty two":
        print ("Yes")
    case _:
        print("No")
