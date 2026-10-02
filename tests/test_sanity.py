def test_something():
    assert 1 + 3 == 4

def test_strings_contain():
    message = "python mastery"
    assert "mastery" in message

def test_arrs():
    expected = [1, 3, 3, 4]
    actual = [1, 3, 3, 3]
    assert expected == actual