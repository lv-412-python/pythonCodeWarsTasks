# -*- coding: utf-8 -*-
"""Example Google style docstrings.
   http://google.github.io/styleguide/pyguide.html

"""

def approxi(num):
    """ modify f(x) to give a good approximation of f(x) in the neigbourhood of 0 """
    return num/2-num**2/8+num**3/16-5/128*num**4+7/256*num**5
