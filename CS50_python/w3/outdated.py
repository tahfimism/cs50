# A list of month names to match against full month name input
list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Start an infinite loop to repeatedly prompt the user until a valid date is entered
while True:
    try:
        # Prompt user input and standardize the format:
        # - strip() removes leading/trailing whitespace
        # - title() capitalizes each word (handles cases like 'september' or 'SEPTEMBER')
        outdate = input("Date: ").strip().title()

        # Check if the input is in numeric MM/DD/YYYY format
        if "/" in outdate:
            # Split by slash and unpack into month, day, and year
            mon, day, year = outdate.split("/")

            # Ensure all parts are digit strings (valid numbers)
            if day.isdigit() and mon.isdigit() and year.isdigit():
                # Convert them to integers for comparison
                day, mon, year = int(day), int(mon), int(year)

                # Check if the day and month are in valid ranges
                if 1 <= day <= 31 and 1 <= mon <= 12:
                    break  # Valid input; exit the loop

        # Otherwise, check if it's in "Month Day, Year" format
        else:
            # Only proceed if there’s a comma (ensures correct format)
            if "," in outdate:
                # Remove the comma and split into components
                mon, day, year = outdate.replace(",", "").split(" ")

                # Check if:
                # - month name is valid (in list)
                # - day and year are numeric
                if mon in list and day.isdigit() and year.isdigit():
                    # Convert month name to its corresponding number (1–12)
                    mon = list.index(mon) + 1

                    # Convert day to integer for range validation
                    day = int(day)

                    # Check if the day is in valid range
                    if 1 <= day <= 31:
                        year = int(year)  # Convert year as well before breaking
                        break  # Valid input; exit the loop

    # If any unpacking or conversion fails (wrong format), ignore and reprompt
    except ValueError:
        pass

# Print the date in ISO format (YYYY-MM-DD), padding month and day with leading 0 if needed
print(f"{year}-{mon:02}-{day:02}")


