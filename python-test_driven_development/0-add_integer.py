#!/usr/bin/python3
"""

Function that adds 2 integers.

"""


def add_integer(a, b=98):
    """
    Args:
        a (int or float): First value.
        b (int or float, optional): Second value. Defaults to 98.

    Raises:
        TypeError: If a or b is not an int or float.

    Returns:
        int: The addition of a and b.
    """

    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
