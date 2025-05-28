from plates import is_valid

def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("CS5005") == True
    assert is_valid("a0053") == False
    assert is_valid("CSgdgdfgdfg") == False
    assert is_valid("50CS") == False   # Doesn't start with letters
    assert is_valid("CS") == True
    assert is_valid("CS05") == False   # Starts with 0
    assert is_valid("CS50P") == False  # Digits followed by letter
    assert is_valid("CS.50") == False  # Non-alphanumeric
    assert is_valid("A") == False      # Too short
    assert is_valid("ABCDEFG") == False # Too long
    assert is_valid("C") == False       # Too short, and not 2 starting letters
    assert is_valid("1C") == False      # Starts with number
    assert is_valid("C1") == False      # Only 1 letter at start


