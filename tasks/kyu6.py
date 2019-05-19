import math


def find_nb(volume):
    """
    Calculates the number of n cubes from building's volume

    Args:
        volume (int): The volume of a building
    Returns:
        int: The return value
    """
    vol = 0
    amount = 1
    while vol != volume:
        vol += math.pow(amount, 3)
        amount += 1
        if vol > volume:
            return -1
    return amount - 1
