# -*- coding: utf-8 -*-
"""Example Google style docstrings.
   http://google.github.io/styleguide/pyguide.html

"""


def sequence_sum(begin_number, end_number, step):
    """ Calculate sum of a sequence """
    return sum(list(range(begin_number, end_number+1, step)))
