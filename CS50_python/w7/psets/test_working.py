from working import convert
import pytest


def test_full_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_with_minutes():
    assert convert("9:30 AM to 5:15 PM") == "09:30 to 17:15"
    assert convert("12:01 AM to 12:59 PM") == "00:01 to 12:59"

def test_edge_cases():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("11:59 AM to 12:00 PM") == "11:59 to 12:00"
    assert convert("11:59 PM to 12:00 AM") == "23:59 to 00:00"


def test_invalid():
    with pytest.raises(ValueError):
        convert("9 to 5 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5 PM")

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM extra text")
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM extra text")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM extra text")  # Extra text should raise an error
def test_invalid_time():
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")  # Invalid minute
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM extra text")  # Extra text should raise an error
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM extra text")  # Extra text should raise an error

def test_invalid_hours():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")  # Invalid hour
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")  # Invalid hour
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM extra text")  # Extra text should raise an error
def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")  # Invalid minute
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM extra text")  # Extra text should raise an error
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM extra text")  # Extra text should raise an error



