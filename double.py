def double(n):
    """Returns the double of n using the standard * operator.
       Sequences and numbers are acceptable input."""
    return n * 2


def test_double_number():
    assert double(2) == 4
    assert double(1.5) == 3


def test_double_string():
    assert double('any') == 'anyany'


def test_double_list():
    assert double([1, 2]) == [1, 2, 1, 2]
