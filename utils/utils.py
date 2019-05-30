"""Utilities for user input of arguments"""

def integer_list_input(length=None):
    """returns list of numbers from user input"""
    input_string = input("Enter a list of {} integers separated by space: "
                         .format(length if length is not None else ""))
    data = [i for i in input_string.split(" ") if i]
    result = []
    if length and len(data) < length:
        result = None
    else:
        for value in data[:length]:
            try:
                result.append(int(value))
            except ValueError:
                print(f"Oops, seems like [{value}] is not an integer")
                result = None
                break
    return result if result else integer_list_input(length)

def float_input(min_val=None, max_val=None, positive=False):
    """Read float number.

    :param min_val: float : minimal value (inclusive).
    :param max_val: float : maximal value (inclusive).
    :param positive: boolean : true if positive number is needed.

    :returns: float : if input is float and fit conditions (if they are).
    :returns: float_input if caught ValueError.
    """
    result = None
    try:
        result = float(input("Enter float number: "))
    except ValueError:
        print("Wrong input. Must be a float number and fit conditions (if they are)")
    if result is not None:
        if min_val and result < min_val:
            print("Wrong input. Number must be greater or equal %.2f" % min_val)
            result = float_input(min_val, max_val, positive)
        if max_val and result > max_val:
            print(f"Wrong input. Number must be less or equal %.2f" % max_val)
            result = float_input(min_val, max_val, positive)
        if positive and result < 0:
            print("Wrong input. Number must be positive or 0")
            result = float_input(min_val, max_val, positive)
    else:
        result = float_input(min_val, max_val, positive)
    return result
