from um import count

def test_simple_um():
    """Tests a single lowercase 'um' and 'um' in a simple sentence."""
    assert count("um") == 1
    assert count("hello, um, world") == 1

def test_um_with_punctuation():
    """Tests 'um' surrounded by or adjacent to punctuation."""
    assert count("um?") == 1
    assert count("um.") == 1
    assert count("um!") == 1
    assert count("Is it um, okay?") == 1
    assert count("um...") == 1 # Test case from problem description
    assert count("um,") == 1
    assert count(",um") == 1
    assert count("(um)") == 1

def test_case_insensitivity():
    """Tests 'um' with various casings."""
    assert count("Um") == 1
    assert count("uM") == 1 # Though less common, good to test
    assert count("UM") == 1
    assert count("Um, thanks for the album.") == 1 # Test case from problem description
    assert count("UM, UM, um") == 3
    assert count("Um... uM? UM!") == 3

def test_multiple_occurrences():
    """Tests strings with multiple instances of 'um'."""
    assert count("um, um, um") == 3
    assert count("Hello um world, um, how are you um?") == 3
    assert count("Um, thanks, um...") == 2 # Test case from problem description
    assert count("um um um um") == 4

def test_um_as_substring_should_be_zero():
    """
    Tests cases where 'um' is a substring of another word.
    These should result in a count of 0.
    """
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("instrument") == 0
    assert count("column") == 0
    assert count("dummy") == 0
    assert count("hummus") == 0
    assert count("circumstance") == 0
    assert count("The sum is large.") == 0 # "sum" contains "um" but is not "um"
    assert count("Number one") == 0

def test_no_um_present():
    """Tests strings that do not contain 'um' as a whole word."""
    assert count("hello world") == 0
    assert count("This is a test without that word.") == 0
    assert count("") == 0 # Test with an empty string
    assert count("u m") == 0 # Test with space in between

def test_um_at_string_edges():
    """Tests 'um' appearing at the very beginning or end of the input string."""
    assert count("um hello world") == 1
    assert count("hello world um") == 1
    assert count("Um. Hello world.") == 1
    assert count("Hello world. Um.") == 1
    assert count("um") == 1 # Already covered, but good for this specific test's focus
