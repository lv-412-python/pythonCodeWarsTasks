# -*- coding: utf-8 -*-
"""Example Google style docstrings.
   http://google.github.io/styleguide/pyguide.html

"""

def desc(sub):
    """ finds lengt of decreasing subsequence """
    result = 0
    for i in range(len(sub)):
        if sub[i] <= sub[i - 1]:
            result += 1
        else:
            break
    result += 1
    return result

def artificial_rain(garden):
    """ finds best spot for artificial rain """
    result_arr = [1]
    for i in range(1, len(garden)-1):
        if garden[i] >= garden[i-1] and garden[i] >= garden[i+1]:
            result_arr.append(desc(garden[i-1::-1])+desc(garden[i::]))
        elif i == 0:
            result_arr.append(desc(garden))
        elif i == len(garden)-1:
            result_arr.append(desc(garden[::-1]))
    return max(result_arr)
