# -*- coding: utf-8 -*-
"""Example Google style docstrings.
   http://google.github.io/styleguide/pyguide.html

"""


def example(first, second):
    """calculate sum a, b.
    Args:
        first (int): The first parameter.
        second (int): The second parameter.

    Returns:
        int: The return value.
    """
    return first + second

def litres(time):
    """
    calculate needed event of water

    Args: time(float)
    Returns : int
    """
    return int(time/2)
