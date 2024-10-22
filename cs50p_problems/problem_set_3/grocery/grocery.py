groceries = {}

while True:
    try:
        item = input().upper()

        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1

    except (KeyError, EOFError):
        for i in sorted(groceries):
            print(groceries[i], i)
        break
