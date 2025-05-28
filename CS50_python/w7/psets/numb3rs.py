import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        parts = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)

        part1 = int(parts.group(1))
        part2 = int(parts.group(2))
        part3 = int(parts.group(3))
        part4 = int(parts.group(4))

        return (part1 < 256 and part2 < 256 and part3 < 256 and part4 <256)
    except AttributeError:
        return False

    # another way to do it
    """
     if not match:
        return False

    for part in match.groups():  # Check ALL parts (not just first)
        if not 0 <= int(part) <= 255:  # Enforce 0–255 range
            return False
    return True
    """    


...


if __name__ == "__main__":
    main()
