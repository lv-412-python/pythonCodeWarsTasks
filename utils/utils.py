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
