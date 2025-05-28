from bank import value

def test_value():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("greetings") == 100
    assert value("Hello") == 0
    assert value("H") == 20
    assert value("h") == 20
    assert value("HELLO") == 0
