# -*- coding: utf-8 -*-
"""Example Google style docstrings.
   http://google.github.io/styleguide/pyguide.html

"""
import math


def solve(limit):
    """
    Calculates x out of sequence "x + 2x**2 + 3x**3 + .. + nx**n"

    Args:
        limit (float or int): The limit of the sequence
    Returns:
        float: The return value
    """
    discriminant = math.pow((1 + 2 * limit), 2) - 4 * limit * limit
    argument = (- (1 + 2 * limit) + math.sqrt(discriminant)) / (-2 * limit)
    return argument

