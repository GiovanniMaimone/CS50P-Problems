#Get user input
camelCase = input("camelCase: ")
print("snake_case: ",end="")

#Tranform camelCase in snake_case
for word in camelCase:
    if word.isupper():
        print("_" + word.lower(), end="")

    else:
        print(word, end="")

print()
