from bank import value

def test_correct_values():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("what's happening") == 100

def test_case_sensitivity():
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("Hey") == 20
    assert value("HEY") == 20

def test_phrase():
    assert value("what's happening") == 100
    assert value("hello , world") == 0
    assert value("good morning") == 100
