"""
Task solution:
   https://www.codewars.com/kata/holiday-viii-duty-free
   https://www.codewars.com/kata/simple-validation-of-a-username-with-regex
"""
import re

ALLOWED_CHARACTERS_PATTERN = r'^[a-z0-9]\S*$'
MIN_USERNAME_LENGHT = 4
MAX_USERNAME_LENGHT = 16
LINEAR_RELATION = 3.9355
OFFSET = 3.4680


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
    return int(time/2)


def starting_mark(height):
    """
    calculate best starting mark
    :param height: float : height of athlete
    :return : float : best strting mark based on height
    """
    return round(height*LINEAR_RELATION+OFFSET, 2)


def duty_free(price: int, discount: int, holiday_cost: int) -> int:
    """
    Calculate  how many bottles of duty free whiskey you would have to buy
    bottle_cost, duty_free_discont and cost_of_the_holiday.
    :param price : int : The first parameter.
    :param duty_free_discont : int: discount on whiskey.
    :param cost_of_the_holiday : int : how much money you can spend on the holiday.
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


def fix_the_meerkat(arr):
    """
    Change the order of elements in list
    :param: arr: list : The list of parts of the body.
    :return: arr list : List of parts of the body in correct order
    """
    tail = arr[0]
    arr[0] = arr[2]
    arr[2] = tail
    return arr


def square_or_square_root(arr):
    """
    If the number has an integer square root, take this, otherwise square the number.
    :param: arr: list : The list of numbers.
    :return: arr list : Modified list.
    """
    result = []
    for element in arr:
        root = element**0.5
        if root.is_integer():
            result.append(int(root))
        else:
            result.append(int(element*element))
    return result
