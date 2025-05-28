import sys

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        sys.exit(0)
    else:
        print("Invalid")
        sys.exit(1)


def is_valid(s):
    # Length check
    if not (2 <= len(s) <= 6):
        return False

    # First two characters must be letters
    if len(s) < 2 or not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Alphanumeric check
    if not s.isalnum():
        return False

    # Digit rules
    for i, c in enumerate(s):
        if c.isdigit():
            if c == '0':
                return False
            if not s[i:].isdigit():
                return False
            break

    return True


if __name__ == "__main__":
    main()
