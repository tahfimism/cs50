def main():
    text = input("Input: ").strip()
    print(shorten(text))


def shorten(word):
    vowels = "aeiouAEIOU"
    novowel = "".join(c for c in word if c not in vowels)
    return novowel


if __name__ == "__main__":
    main()
