# test_seasons.py
import pytest
from datetime import date
from seasons import minute # Import your modified minute function

# Define a fixed "today" date for consistent testing
FIXED_TODAY_DATE = date(2025, 5, 27)

def test_valid_dates():
    """Tests the function with valid date inputs by directly passing values."""

    # Test Case 1: Birth date 2022-11-22
    # Days between 2022-11-22 and 2025-05-27 = 917 days
    # Minutes = 917 * 24 * 60 = 1,320,480
    assert minute("2022-11-22", FIXED_TODAY_DATE) == "One million, three hundred twenty thousand, four hundred eighty minutes"

    # Test Case 2: Birth date 2024-05-27 (exactly one year ago)
    # Days = 365. Minutes = 525,600
    assert minute("2024-05-27", FIXED_TODAY_DATE) == "Five hundred twenty-five thousand, six hundred minutes"



def test_invalid_date_format():
    """Tests inputs that are not in YYYY-MM-DD format."""

    invalid_formats = [
        "January 1, 2000",
        "2000/01/01",
        "2000_01_01",
        "cat",
        "2023-10",        # Not enough parts
        "2023-10-25-extra" # Too many parts
    ]
    for invalid_input_str in invalid_formats:
        with pytest.raises(SystemExit) as e:
            minute(invalid_input_str, FIXED_TODAY_DATE)
        assert str(e.value) == "Invalid Date"

def test_invalid_date_values():
    """Tests YYYY-MM-DD format but with impossible date values or future dates."""

    invalid_values = [
        "2000-13-01",  # Invalid month
        "2000-01-32",  # Invalid day
        "1999-02-29",  # 1999 is not a leap year
        "2026-01-01"   # Future date relative to FIXED_TODAY_DATE
    ]
    for invalid_input_str in invalid_values:
        with pytest.raises(SystemExit) as e:
            minute(invalid_input_str, FIXED_TODAY_DATE)
        assert str(e.value) == "Invalid Date"
