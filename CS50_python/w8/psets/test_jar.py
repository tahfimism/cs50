import pytest
from jar import Jar # Assuming your Jar class is in a file named jar.py

def test_init():
    """Tests the initialization of the Jar class."""
    # Test default capacity and size
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test custom capacity
    jar_custom_cap = Jar(capacity=5)
    assert jar_custom_cap.capacity == 5
    assert jar_custom_cap.size == 0 # Default size should still be 0

    # Test custom initial size (within default capacity)
    jar_initial_size = Jar(size=3)
    assert jar_initial_size.capacity == 12 # Default capacity
    assert jar_initial_size.size == 3


    # Test custom initial size and capacity
    jar_all_custom = Jar(capacity=10, size=5)
    assert jar_all_custom.capacity == 10
    assert jar_all_custom.size == 5

    # Test ValueError for invalid initial capacity (negative or non-integer) - though not explicitly handled by your setter,
    # Python's default int conversion would raise ValueError for non-int.
    # Your current setter for capacity doesn't validate positive integer, but it's good practice.
    # We will test for the size setter's ValueError for invalid initial size.
    with pytest.raises(ValueError, match="invalid house"):
        Jar(capacity=5, size=6) # Initial size exceeds initial capacity

    with pytest.raises(ValueError, match="invalid house"):
        Jar(size=13) # Initial size exceeds default capacity (12)


def test_str():
    """Tests the __str__ method for correct cookie representation."""
    jar = Jar()
    assert str(jar) == "" # Empty jar

    jar.deposit(1)
    assert str(jar) == "🍪" # Jar with one cookie

    jar.deposit(11) # Deposit 11 more to reach full capacity (1 + 11 = 12)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪" # Full jar

    jar_empty_custom = Jar(capacity=5, size=0)
    assert str(jar_empty_custom) == ""
    jar_empty_custom.deposit(5)
    assert str(jar_empty_custom) == "🍪🍪🍪🍪🍪"


def test_deposit():
    """Tests the deposit method for adding cookies and handling errors."""
    jar = Jar()

    # Test valid deposit
    jar.deposit(5)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"

    # Test depositing to full capacity
    jar.deposit(7) # 5 + 7 = 12
    assert jar.size == 12
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    # Test ValueError when depositing too much (exceeds capacity)
    with pytest.raises(ValueError, match="jar full"):
        jar.deposit(1) # Try to add one more to a full jar

    # Test depositing into a custom capacity jar
    jar_custom = Jar(capacity=5)
    jar_custom.deposit(3)
    assert jar_custom.size == 3
    jar_custom.deposit(2)
    assert jar_custom.size == 5
    with pytest.raises(ValueError, match="jar full"):
        jar_custom.deposit(1)


def test_withdraw():
    """Tests the withdraw method for removing cookies and handling errors."""
    jar = Jar()
    jar.deposit(10) # Start with 10 cookies

    # Test valid withdrawal
    jar.withdraw(3)
    assert jar.size == 7
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"

    # Test withdrawing all remaining cookies
    jar.withdraw(7)
    assert jar.size == 0
    assert str(jar) == ""

    # Test ValueError when withdrawing from an empty jar
    with pytest.raises(ValueError, match="jar empty"):
        jar.withdraw(1)

    # Test ValueError when withdrawing more than available
    jar_partial = Jar()
    jar_partial.deposit(5)
    with pytest.raises(ValueError, match="jar empty"): # Your error message is "jar empty" even if it's "jar not enough cookies"
        jar_partial.withdraw(6)
