import re
import sys


def main():
    print(count(input("Text: ")))

# hello, um, world

def count(s):
    matches = re.findall(r"\bum\b", s.strip(), re.IGNORECASE)
    return len(matches)


...


if __name__ == "__main__":
    main()
