# -*- coding: utf-8 -*-
"""Example Google style docstrings.
   http://google.github.io/styleguide/pyguide.html

"""
def fix_the_meerkat(arr):
    """
    Args:
        arr (list): The list of parts of the body.
    Returns:
        arr (list): Ordered list of parts of the body.
    """
    tail = arr[0]
    arr[0] = arr[2]
    arr[2] = tail
    return arr
