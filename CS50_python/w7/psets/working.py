import re
import sys


def main():
    print(convert(input("Hours: ")))

"""
9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
"""

def convert(s):
    time = re.fullmatch(r"(\d{1,2})(:\d{2})? (AM|PM) to (\d{1,2})(:\d{2})? (AM|PM)", s.strip())

    if not time:
        raise ValueError

    starth = int(time.group(1))
    startm = time.group(2) or ":00"
    starti = time.group(3)

    endh = int(time.group(4))
    endm = time.group(5) or ":00"
    endi = time.group(6)

    if starth > 12 or endh > 12 or startm > ":59" or endm > ":59":
        raise ValueError

    if starti == "AM" and starth == 12:
        starth = 0
    elif starti == "PM" and starth < 12:
        starth += 12

    if endi == "AM" and endh == 12:
        endh = 0
    elif endi == "PM" and endh < 12:
        endh += 12

    if (starth == endh and startm > endm):
        raise ValueError

    return f"{starth:02}{startm} to {endh:02}{endm}"


...


if __name__ == "__main__":
    main()
