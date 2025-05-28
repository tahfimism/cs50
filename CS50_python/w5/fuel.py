import sys

def convert(fraction):
    try:
        x_str, y_str = fraction.strip().split("/")
        x, y = int(x_str), int(y_str)
    except ValueError:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    if x > y:
        raise ValueError

    percentage = (x / y) * 100
    return round(percentage)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"

def main():
    fraction = input("Fraction: ")
    try:
        pct = convert(fraction)
    except (ValueError, ZeroDivisionError):
        sys.exit(1)
    print(gauge(pct))

if __name__ == "__main__":
    main()
