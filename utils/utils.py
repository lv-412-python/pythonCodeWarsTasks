"""Utilities for user input of arguments"""

def integer_list_input(length=None):
    """returns list of numbers from user input
    :param length: int: needed length of list
    :returns: list: if result != None else integer_list_input(length)"""
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


def float_input(minimum=None, maximum=None, positive=False):
    """Read float number.

    :param minimum: float : minimal value (inclusive).
    :param maximum: float : maximal value (inclusive).
    :param positive: boolean : true if positive number is needed.

    :returns: float : if input is float and fit conditions (if they are).
    :returns: float_input if caught ValueError.
    """
    result = None
    try:
        result = float(input("Enter float number: "))
    except ValueError:
        print("Incorrect input, must be float that fit conditions (if conditions exist)!")
    if result is not None:
        if minimum and result < minimum:
            print("Incorrect input. Number must be greater or equal %.2f" % minimum)
            result = float_input(minimum, maximum, positive)
        if maximum and result > maximum:
            print("Incorrect input. Number must be less or equal %.2f" % maximum)
            result = float_input(minimum, maximum, positive)
        if positive and result < 0:
            print("Incorrect input. Number must be positive or 0")
            result = float_input(minimum, maximum, positive)
    else:
        result = float_input(minimum, maximum, positive)
    return result

def integer_input(minimum=None, maximum=None, positive=False):
    """Read integer number.

    :param minimum: int : minimal value (inclusive).
    :param maximum: int : maximal value (inclusive)
    :param positive: boolean : true if positive number is needed.

    :returns: int : if input is int and fit conditions (if they are).
    :returns: integer_input if caught ValueError.
    """
    data = None
    try:
        data = int(input("Enter integer please: "))
    except ValueError:
        print('Incorrect input, must be only integers that fit conditions (if conditions exist)!')
    if data is not None:
        if minimum and data < minimum:
            print("Incorrect input. Number must be greater or equal %d" % minimum)
            data = integer_input(minimum, maximum, positive)
        if maximum and data > maximum:
            print("Incorrect input. Number must be less or equal %d" % maximum)
            data = integer_input(minimum, maximum, positive)
        if positive and data < 0:
            print("Incorrect input. Number must be positive or 0")
            data = integer_input(minimum, maximum, positive)
    else:
        data = integer_input(minimum, maximum, positive)
    return data
