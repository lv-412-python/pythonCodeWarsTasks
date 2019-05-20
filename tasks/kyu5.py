# -*- coding: utf-8 -*-
"""Example Google style docstrings.
   http://google.github.io/styleguide/pyguide.html
"""

def zeros(num):
    """
    Args:
        number(int) - num
    Returns:
        Calculate the number of trailing zeros in a factorial of a given number and return number.
    """
    i = 5
    num_of_zeros = 0
    while num >= i:
        num_of_zeros += num // i
        i *= 5
    return num_of_zeros
