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

def starting_mark(height):
    """
    Calculate needed starting_mark
    Args:
         height(float)
    Returns:
	 float
    """
    linear_relation = 3.9355
    offset = 3.4680
    return round(height*linear_relation+offset, 2)
