# -*- coding: utf-8 -*-
"""Example Google style docstrings.
   http://google.github.io/styleguide/pyguide.html

"""

def replicate(times, number):
    """
    Args:
        times, number.
    Returns:
        Function should return an array containing
        repetitions of the number argument
    """
    if times <= 0:
        return []
    if times == 1:
        return [number]
    list_of_nums = [number]
    return list_of_nums + replicate(times-1, number)
