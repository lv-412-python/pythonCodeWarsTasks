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


def divisible_by(array, divisor):
    """
        Returns a list of numbers which are divisible by given number
        Args:
            array (list): The first parameter
            divisor (int): The second parameter
        Returns:
            list: The return value
    """
    return_list = list()
    for i in array:
        if i % divisor == 0:
            return_list.append(i)
    return return_list
