"""
Implementation of short long short string concatenation.
"""


def short_long_short(first_str, second_str):
    """
    Concatenates strings in a specific order (short + long + short).
    """
    if len(first_str) > len(second_str):
        return ''.join(second_str + first_str + second_str)
    return ''.join(first_str + second_str + first_str)
