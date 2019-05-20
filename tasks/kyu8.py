# -*- coding: utf-8 -*-
"""Example Google style docstrings.
   http://google.github.io/styleguide/pyguide.html

"""
def square_or_square_root(arr):
    """
    Args:
        arr (list): The list of numbers.
    Returns:
        arr (list): If the number has an integer square root,
        take this, otherwise square the number.
    """
    result = []
    for num in arr:
        root = num**0.5
        if root.is_integer():
            result.append(int(root))
        else:
            result.append(int(num*num))
    return result
