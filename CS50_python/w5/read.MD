# p/w5/ README

This folder contains Python scripts for Week 5 exercises and problem sets, including code and tests. Here is a description of each file:

## Main Scripts
- **bank.py**: Prompts for a greeting and prints a dollar amount based on whether the greeting starts with "hello", "h", or something else. Uses a helper function for logic.
- **fuel.py**: Prompts for a fuel fraction (like 1/4), converts it to a percentage, and prints a gauge (E, F, or percent). Handles invalid input and division by zero.
- **plates.py**: Checks if a given string is a valid license plate according to specific rules and prints "Valid" or "Invalid". Exits with code 1 for invalid input.
- **twttr.py**: Prompts for input and prints the string with all vowels removed.

## Test Files
- **test_bank.py**: Tests the `value` function from bank.py for various greetings.
- **test_fuel.py**: Tests the `convert` and `gauge` functions from fuel.py, including valid, invalid, and edge cases.
- **test_plates.py**: Tests the `is_valid` function from plates.py with a variety of valid and invalid license plates.
- **test_twttr.py**: Tests the `shorten` function from twttr.py for different input strings.

---

Each script is a standalone program for practicing string manipulation, validation, and writing unit tests in Python.
