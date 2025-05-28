# seasons.py
from datetime import date
import sys
import inflect

p = inflect.engine()

# The minute function now takes optional arguments for testing
def minute(birth_date_str=None, today_date=None):
    """
    Calculates age in minutes from a birth date.
    If birth_date_str is None, it prompts the user for input.
    If today_date is None, it uses the current date.
    """
    if birth_date_str is None:
        birth_date_str = input("Date of Birth: ").strip()

    try:
        year, mon, day = map(int, birth_date_str.split("-"))
        birth = date(year, mon, day)
    except ValueError:
        sys.exit("Invalid Date")

    if today_date is None:
        today_date = date.today()

    if birth > today_date:
        sys.exit("Invalid Date") # Changed from 'future birth date' for consistent error message

    c = today_date - birth
    count = c.days

    # The negative check for count is redundant if birth > today_date is handled
    # but keeping it as a safeguard if other logic changes
    if count < 0:
        sys.exit("Invalid Date")

    total_minutes = count * 24 * 60
    # Ensure capitalization and 'and' removal match the tests
    return f"{p.number_to_words(total_minutes, andword="").capitalize()} minutes"

def main():
    print(minute())

if __name__ == "__main__":
    main()
