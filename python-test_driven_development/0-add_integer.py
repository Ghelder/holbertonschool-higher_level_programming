#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Args:
        a: first arguments
        b: second arguments
    validate numbers:
        the arguments a or b must be integers or floats
    TypeError:
        If the arguments a or b is not an integer or a float value
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
