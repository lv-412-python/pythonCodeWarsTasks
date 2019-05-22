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
        :param point: Point: object of type Circle
        :param radius: int or float: the radius of the Circle
        """
        self._point = point
        self._radius = radius

    @property
    def point(self):
        """
        :returns: str
        """
        return self._point

    @property
    def radius(self):
        """
        :returns: float or int
        """
        return self._radius


class Point:
    """
    A class used to represent a Point
    """

    def __init__(self, x_point, y_point):
        """
        :param x_point: int or float: The coordinate of x.
        :param x_point: int or float: The coordinate of y.
        """
        self._x = x_point
        self._y = y_point

    @property
    def x_point(self):
        """
        :returns: int or float
        """
        return self._x

    @property
    def y_point(self):
        """
        :returns: int or float
        """
        return self._y


def circle_area(circle):
    """"
    Calculates the area of a circle
    :param circle: Circle: object of type Circle.
    :returns float: area of the circle.
    """
    return math.pi * circle.radius * circle.radius
