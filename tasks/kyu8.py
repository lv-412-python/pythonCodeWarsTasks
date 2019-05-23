"""
Implementation of short long short string concatenation.
"""


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

LINEAR_RELATION = 3.9355
OFFSET = 3.4680
def starting_mark(height):
    """
    calculate best starting mark
    :param height: float : height of athlete
    :return : float : best strting mark based on height
    """
    return round(height*LINEAR_RELATION+OFFSET, 2)
