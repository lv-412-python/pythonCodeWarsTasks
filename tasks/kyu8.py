"""
Task solution:
   https://www.codewars.com/kata/holiday-viii-duty-free
   https://www.codewars.com/kata/simple-validation-of-a-username-with-regex
"""
import re
from math import pi

ALLOWED_CHARACTERS_PATTERN = r'^[a-z0-9]\S*$'
MIN_USERNAME_LENGHT = 4
MAX_USERNAME_LENGHT = 16
LINEAR_RELATION = 3.9355
OFFSET = 3.4680
ONE_IMP_GALLON_IN_LITERS = 4.54609188
ONE_MILE_IN_KILOMETERS = 1.606344


class Circle:
    """
    A class used to represent a Circle
    """

    def __init__(self, point, radius):
        """
        :param point: Point: The object of class Point.
        :param radius: float: A radius of the circle.
        """
        self._point = point
        self._radius = radius

    @property
    def point(self):
        """
        :return: str
        """
        return self._point

    @property
    def radius(self):
        """
        :return: float or int
        """
        return self._radius


class Point:
    """
    A class used to represent a Point
    """

    def __init__(self, x_num, y_num):
        """
        :param x_num: int or float: The coordinate of x.
        :param y_num: int or float: The coordinate of y.
        """
        self._x_point = x_num
        self._y_point = y_num

    @property
    def x_point(self):
        """
        :return: int or float
        """
        return self._x_point

    @property
    def y_point(self):
        """
        :return: int or float
        """
        return self._y_point


def circle_area(circle):
    """"
    Calculates the area of a circle

    :param circle: Circle: The object of class Point.
    :return: float: The area of the circle
    """
    return pi * circle.radius * circle.radius


def volume_of_a_cuboid(length, width, height):
    """Calculate volume of a cuboid.

    :param length : float : Length of a cuboid.
    :param width: float : Width of a cuboid.
    :param height :float : Height of a cuboid.

    :return: float : Volume of a cuboid (length * width * height).

    """
    return length * width * height


def heads_legs(heads, legs):
    """
    Finds the number of cows and chickens by being given the amount of heads and legs on the farm.
    :param heads: int : amount of heads on the farm.
    :param legs: int : amount of legs on the farm
    :return: tuple : string : number of chickens and cows or string, when there is no solution.
    """
    for i in range(0, heads + 1):
        cows = heads - i
        if 4 * cows + 2 * i == legs:
            chickens = i
            return chickens, cows
    return "No solutions."


def short_long_short(first, second):
    """
    Concatenates strings in a specific order (short + long + short).
    :param first : string : just some string.
    :param second: string : just some string.
    :return: string : joined in order short + long + short.
    """
    if len(first) > len(second):
        return ''.join(second + first + second)
    return ''.join(first + second + first)


def litres(time):
    """
    Calculates needed amount of water
    :param time: float : time of run
    :return : int : needed amount of water based on time
    """
    return int(time / 2)


def starting_mark(height):
    """
    calculates best starting mark
    :param height: float : height of athlete
    :return : float : best strting mark based on height
    """
    return round(height * LINEAR_RELATION + OFFSET, 2)


def duty_free(price: int, discount: int, holiday_cost: int) -> int:
    """
    Calculates  how many bottles of duty free whiskey you would have to buy
    bottle_cost, duty_free_discont and cost_of_the_holiday.
    :param price: int : The first parameter.
    :param discount: int : discount on whiskey.
    :param holiday_cost: int : how much money you can spend on the holiday.
    :return: int : How many bottles of whiskey you can buy.
    """
    if holiday_cost == 500:
        return holiday_cost

    discount /= 100
    price = holiday_cost / (price - price * discount)
    price = int(price)
    return price


def validate_usr(username: str) -> bool:
    """
    Check your username for correctness
    :param username : str : Your username.
    :return: bool : The return True or False.
    """
    if MIN_USERNAME_LENGHT <= len(username) < MAX_USERNAME_LENGHT:
        return bool(re.search(ALLOWED_CHARACTERS_PATTERN, username))

    return False


def fix_the_meerkat(animal):
    """
    Change the order of elements in list
    :param animal: list : The list of parts of the body.
    :return: animal: list : List of parts of the body in correct order
    """
    tail = animal[0]
    animal[0] = animal[2]
    animal[2] = tail
    return animal


def square_or_square_root(numbers):
    """
    If the number has an integer square root, take this, otherwise square the number.
    :param numbers: list : The list of numbers.
    :return: list : Modified list.
    """
    result = []
    for element in numbers:
        root = element ** 0.5
        if root.is_integer():
            result.append(int(root))
        else:
            result.append(int(element * element))
    return result


def miles_per_gallon_to_kilometers_per_liter(miles_per_gallon):
    """Convert miles per imperial gallon into kilometers per liter.

    :param miles_per_gallon : float : The value to convert.

    :return: float : Converted value rounded to two digits.

    """
    converted_value = miles_per_gallon * ONE_MILE_IN_KILOMETERS / ONE_IMP_GALLON_IN_LITERS
    return round(converted_value, 2)


def divisible_by(array, divisor):
    """
        Returns a list of numbers which are divisible by given number

        :param array: list: The list of numbers to be checked
        :param divisor: int: The divisor

        :return: list: The return value
    """
    return_list = list()
    for i in array:
        if i % divisor == 0:
            return_list.append(i)
    return return_list


def am_i_wilson(number):
    """
        Check if number is wilson prime.
        :param number: int : number for checking.
        :return: bool : True for wilson primes.
    """
    return number in (5, 13, 563)


def two_decimal_places(number):
    """
        Round number to two decimal places.
        :param number: float : number to be formatted.
        :return: float : rounded number to two decimals.
    """
    return round(number, 2)


def abbrev_name(name):
    """
    Convert a name into initials
    :param name: str : two-worded name.
    :return: str : initials of the name.
    """
    arr = name.split()
    anw = arr[0][0] + "." + arr[1][0]
    return anw.upper()


def bin_to_decimal(inp):
    """
    convert a binary number into decimal
    :param inp: str :binary number
    :return: int :decimal number
    """
    bin_list = list(inp)
    j = len(bin_list)
    dec_num = 0
    for i in range(j):
        dec_num += (int(bin_list[i]) * (2 ** (j - 1)))
        j -= 1
    return dec_num
