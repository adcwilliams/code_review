"""Pytest functions
"""
import my_function

def test_addition():
    """Test the add_integers() function."""

    # Choose known arguments, 13, and 7, which will return a result of 20.
    assert my_function.add_integers(13, 7) == 20
