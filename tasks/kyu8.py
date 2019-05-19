# -*- coding: utf-8 -*-
"""Example Google style docstrings.
   http://google.github.io/styleguide/pyguide.html

"""
import math


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


class Circle:
    """
    A class used to represent a Circle
    """

    def __init__(self, point, radius):
        """
        Args:
            point (Point): The first parameter
            radius (float): The second parameter
        """
        self._point = point
        self._radius = radius

    @property
    def point(self):
        """
        returns: str
        """
        return self._point

    @property
    def radius(self):
        """
        returns: float or int
        """
        return self._radius


class Point:
    """
    A class used to represent a Point
    """

    def __init__(self, x, y):
        """
        Args:
            x (int or float): The first parameter
            y (int or float): The second parameter
        """
        self._x = x
        self._y = y

    @property
    def x(self):
        """
        returns: int or float
        """
        return self.x

    @property
    def y(self):
        """
        returns: int or float
        """
        return self.y


def circle_area(circle):
    """"
    Calculates the area of a circle

    Args:
        circle (Circle)
    Returns:
        float: The return value
    """
    return math.pi * circle.radius * circle.radius
