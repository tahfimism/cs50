import re
import sys


def main():
    print(convert(input("Hours: ")))

"""
In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.
9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
"""

def convert(s):

    times = re.fullmatch(r"(\d{1,2})(:\d{2})? (AM|PM) to (\d{1,2})(:\d{2})? (AM|PM)", s.strip())

    if not times:
        raise ValueError

    starth = int(times.group(1))
    startm = times.group(2) or ":00"
    starti = times.group(3)

    endh = int(times.group(4))
    endm = times.group(5) or ":00"
    endi = times.group(6)

    if starth > 12 or endh > 12 or startm > ":59" or endm > ":59":  # Check for valid hour and minute ranges
        raise ValueError

    if starti == "AM":
        if starth == 12:
            starth = 0
    else:  # PM
        if starth < 12:
            starth += 12

    if endi == "AM":
        if endh == 12:
            endh = 0
    else:  # PM
        if endh < 12:
            endh += 12
    if (starth == endh and startm > endm):
        raise ValueError





    return f"{starth:02}{startm} to {endh:02}{endm}"



...


if __name__ == "__main__":
    main()
