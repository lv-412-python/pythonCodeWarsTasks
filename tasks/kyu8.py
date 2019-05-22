# -*- coding: utf-8 -*-

"""
Implement task solution for 8kyu:
   https://www.codewars.com/kata/simple-validation-of-a-username-with-regex
"""

import re

ALLOWED_CHARACTERS_PATTERN = r'^[a-z0-9]\S*$'
MIN_USERNAME_LENGHT = 4
MAX_USERNAME_LENGHT = 16


def validate_usr(username: str) -> bool:
    """Check your username for correctness
    Args:
        username (str): Your username.
    Returns:
        bool: The return True or False.
    """
    if MIN_USERNAME_LENGHT <= len(username) < MAX_USERNAME_LENGHT:
        return bool(re.search(ALLOWED_CHARACTERS_PATTERN, username))

    return False


def short_long_short(first_str, second_str):
    """
    Concatenates strings in a specific order (short + long + short).
    """
    if len(first_str) > len(second_str):
        return ''.join(second_str + first_str + second_str)
    return ''.join(first_str + second_str + first_str)
