# -*- coding: utf-8 -*-
"""Example Google style docstrings.
   http://google.github.io/styleguide/pyguide.html

"""

def desc(sub):
    """ counts descending subsequence """
    result = 0
    for i in enumerate(sub):
        if sub[i[0]] <= sub[i[0] - 1]:
            result += 1
        else:
            break
    result += 1
    return result


def artificial_rain(garden):
    """ counts longest descending subsequence """
    result_arr = [1]
    if len(garden) == 1:
        return 1
    result_arr.append(desc(garden))
    result_arr.append(desc(garden[::-1]))
    for i in enumerate(garden[:-1]):
        if garden[i[0]] >= garden[i[0] - 1] and garden[i[0]] >= garden[i[0] + 1]:
            result_arr.append(desc(garden[i[0] - 1::-1]) + desc(garden[i[0]::]))
    return max(result_arr)
