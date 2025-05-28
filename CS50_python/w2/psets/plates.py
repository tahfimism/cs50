def main():
     plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6 and s[0].isalpha() and s[1].isalpha() and s.isalnum()):
        return False
    digit_started = False
    for c in range(len(s)):
        if s[c].isdigit():
            if not digit_started:
                if s[c] == "0":
                    return False
            digit_started = True
        elif digit_started:
            return False
    return True


if __name__ == "__main__":
    main()
