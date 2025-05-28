from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("Python") == "Pythn"
    assert shorten("pytHon") == "pytHn"
    assert shorten("") == ""
    assert shorten("12345") == "12345"
    assert shorten("!@#$%^&*()") == "!@#$%^&*()"
    assert shorten("hello world") == "hll wrld"
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("Python is fun") == "Pythn s fn"
    assert shorten("pytHon is fUn") == "pytHn s fn"



