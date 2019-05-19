# -*- coding: utf-8 -*-
"""Task solution:
   https://www.codewars.com/kata/simple-validation-of-a-username-with-regex
"""
import re

ALLOWED_CHARACTERS_PATTERN = '^[a-z0-9]\S*$'
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
        result = re.search(ALLOWED_CHARACTERS_PATTERN, username)
        if result:
            return True
        else:
            return False

    else:
        return False
