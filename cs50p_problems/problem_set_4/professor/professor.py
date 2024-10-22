import random


def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level
def generate_integer(level):
    score = 0
    for _ in range(10):
        if level == 1:
            x = int(random.randint(0,9))
            y = int(random.randint(0,9))
        elif level == 2:
            x = int(random.randint(10,99))
            y = int(random.randint(10,99))
        else:
            x = int(random.randint(100,999))
            y = int(random.randint(100,999))

        answer_inc = 1
        while answer_inc <= 3:
                answer = int(input(f"{x} + {y} = "))
                if answer == (x + y):
                    score += 1
                    break
                elif answer != (x + y) and answer_inc != 3:
                    print("EEE")
                    answer_inc += 1
                else:
                    print("EEE")
                    print(f"{x} + {y} = {x + y}")
                    break
    print(f"Score: {score}")


if __name__ == "__main__":
    main()
