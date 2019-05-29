"""Utilities"""

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


def float_input(min_val = None, max_val = None, positive = False):
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

def read_integer(minimum=None, maximum=None, positive=False):
    """Read int number. Can take arguments:
    :param args[0]: int : max value.
    or
    :param args[0]: int : min value.
    :param args[1]: int : max value.

    :param kwargs["positive"]: boolean : True if positive number is needed.

    :returns: int : if input is int and fit conditions (if they are).
    :returns: int_input() if caught ValueError.
    """
    data = None
    try:
        data = int(input("Enter integer please: "))
    except ValueError:
        print('Incorrect input, must be only integers that fit conditions (if conditions exists)!')
    if data is not None:
        if minimum and data < minimum:
            print('Wrong input, must be only integers that fit conditions (if conditions exists)!')
            data = read_integer(minimum, maximum, positive)
        if maximum and data > maximum:
            print('Wrong input, must be only integers that fit conditions (if conditions exists)!')
            data = read_integer(minimum, maximum, positive)
        if positive and data < 0:
            print('Wrong input, must be only integers that fit conditions (if conditions exists)!')
            data = read_integer(minimum, maximum, positive)
    else:
        data = read_integer(minimum, maximum, positive)
    return data

