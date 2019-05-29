"""Utilities for main.py"""

def numeric_list_input(length=None):
    """returns list of numbers from user input"""
    input_string = input("Enter a list of {} integers separated by space: "
                         .format(length if length is not None else ""))
    data = [i for i in input_string.split(" ") if i]
    result = []
    for value in data[:length]:
        try:
            value = int(value)
        except ValueError:
            print(f"Oops, seems like [{value}] is not an integer")
        if isinstance(value, str):
            result = numeric_list_input(length)
            break
        result.append(value)
    return numeric_list_input(length) if result == [] else result

def float_input(min = 0, max = 999999, positive = False):
    """Read float number.

    :param min: float : minimal value.
    :param max: float : maximal value.
    :param positive: boolean : true if positive number is needed.

    :returns: float : if input is float and fit conditions (if they are).
    :returns: float_input if caught ValueError.
    """
    result = float()

    try:
        result = float(input("Enter float number: "))
        if result < min or result > max:# or args[0] > args[1]:
            raise ValueError

        if positive and result < 0:
            raise ValueError

    except ValueError:
        print("Wrong input. Must be a float number and fit conditions (if they are)")
        result = float_input(min, max, positive)

    return result
