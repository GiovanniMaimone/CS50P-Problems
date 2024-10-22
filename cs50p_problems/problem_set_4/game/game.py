import random

while True:
    try:
        level = int(input("Level: "))

        if level > 0:
            break
    except:
        pass

randonint = int(random.randint(1,level))

while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess < randonint:
                    print("Too small!")
                elif guess > randonint:
                    print("Too large!")
                elif guess == randonint:
                    print("Just right!")
                    break
        except:
            pass
