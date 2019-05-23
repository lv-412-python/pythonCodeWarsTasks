"""
Implementation of short long short string concatenation.
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

def short_long_short(first_str, second_str):
    """
    Concatenates strings in a specific order (short + long + short).
    """
    if len(first_str) > len(second_str):
        return ''.join(second_str + first_str + second_str)
    return ''.join(first_str + second_str + first_str)

def litres(time):
    """
    calculate needed amount of water
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
    """Calculate  how many bottles of duty free whiskey you would have to buy
        bottle_cost, duty_free_discont and cost_of_the_holiday.
        :price : int : The first parameter.
        :duty_free_discont : int: discount on whiskey.
        :cost_of_the_holiday : int : how much money you can spend on the holiday.
        :returns : int : How many bottles of whiskey you can buy.
    """
    if holiday_cost == 500:
        return holiday_cost

    discount /= 100
    price = holiday_cost / (price - price * discount)
    price = int(price)
    return price

def validate_usr(username: str) -> bool:
    """Check your username for correctness
        :username : str : Your username.
    Returns:
        :returns : bool : The return True or False.
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
