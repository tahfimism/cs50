
words = { 'hair': 4, 'chair': 5, 'pair' : 4}

def main():
    print("welcome to spell bee")

    sum = 0
    life = 3
    while len(words) > 0:
        print(f"u have {len(words)} words left to guess")
        print(f"u have {life} wrong try left")
        guess = input("guess a word ")


        if guess in words.keys():
            points = words.pop(guess)
            sum = sum + points
            print(f"ur points: {sum}")

        else:
            life = life - 1
            if life == 0:
                print("sily u lost")
                break
            else:
                print(f"wrong, u have {life} try left")
    if sum == 13:
        print("good job")












main()
