from numb3rs import validate

def test_valid_ips():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True

def test_invalid_ips():
    # Invalid formats
    assert validate("cat") == False
    assert validate("1.2.3.4.5") == False
    assert validate("192.168.1") == False

    # Numbers out of range (0-255)
    assert validate("256.0.0.0") == False
    assert validate("0.256.0.0") == False  # Added: Second part invalid
    assert validate("0.0.256.0") == False  # Added: Third part invalid
    assert validate("0.0.0.256") == False  # Added: Fourth part invalid
    assert validate("255.255.255.300") == False

def test_non_numeric_parts():
    assert validate("192.168.one.1") == False
