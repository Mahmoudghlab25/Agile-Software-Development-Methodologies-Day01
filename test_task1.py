from task1 import get_sum_from_string

def test_standard_addition():
    assert get_sum_from_string("10+20") == 30

def test_addition_with_spaces():
    assert get_sum_from_string("  5 + 5  ") == 10

def test_negative_numbers():
    assert get_sum_from_string("10 + -5") == 5

def test_invalid_input_returns_zero():
    assert get_sum_from_string("invalid") == 0