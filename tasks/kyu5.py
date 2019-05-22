# -*- coding: utf-8 -*-
"""
kyu7tasks
"""
import math


def solve(limit):
    """
    Calculates x out of sequence 'x + 2x**2 + 3x**3 + .. + nx**n'

    :param limit: float : The limit of the sequence.
    :return: float : argument of the sequence.
    """
    discriminant = math.pow((1 + 2 * limit), 2) - 4 * limit * limit
    argument = (- (1 + 2 * limit) + math.sqrt(discriminant)) / (-2 * limit)
    return argument
