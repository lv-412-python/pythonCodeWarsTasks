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

    def __init__(self, x_point, y_point):
        """
        Args:
            x_point (int or float): The first parameter
            y_point (int or float): The second parameter
        """
        self._x = x_point
        self._y = y_point

    @property
    def x_point(self):
        """
        returns: int or float
        """
        return self._x

    @property
    def y_point(self):
        """
        returns: int or float
        """
        return self._y


def circle_area(circle):
    """"
    Calculates the area of a circle

    Args:
        circle (Circle)
    Returns:
        float: The return value
    """
    return math.pi * circle.radius * circle.radius
