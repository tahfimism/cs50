import random


def main():

    level = get_level() # Get level from user
    score = 0           # Initialize score to 0

    for i in range(10):                 # Loop 10 times
                                        # Generate two random integers based on level
        n1 = generate_integer(level)
        n2 = generate_integer(level)
        sum = n1 + n2                   # Calculate the sum of the two integers


        trying = 0
        while trying < 3:
            try:
                print(f"{n1} + {n2} = ", end="")
                ans = int(input())
                if ans == sum:
                    score = score + 1
                    break
                else:
                    print("EEE")
                    trying += 1
            except ValueError:
                print("EEE")
                trying += 1
        if trying == 3:
            print(f"{n1} + {n2} = {sum}")

    print(f"Score: {score}")




def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
