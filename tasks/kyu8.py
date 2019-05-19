"""
Implementation of short long short string concatenation.
Task solution:
   https://www.codewars.com/kata/holiday-viii-duty-free
"""
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
