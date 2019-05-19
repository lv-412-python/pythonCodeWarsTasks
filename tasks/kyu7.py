# -*- coding: utf-8 -*-
"""
    Task solution:
   https://www.codewars.com/kata/easy-line
"""
from math import ceil


def series_sum(nth_num):
    """
    Calculates the sum of the series upto nth term

    :param nth_num: int: nth term of the series
    :return: str: sum of the series
    """
    if nth_num == 0:
        return format(0, '.2f')
    series = 1
    divisor = 4
    for _ in range(0, nth_num - 1):
        series += 1 / divisor
        divisor += 3
    return format(series, '.2f')


def triple_shiftian(first_three_elements, num):
    """
    Finds the n-th element from Triple Shiftian.
    :param first_three_elements: list : list with first three elements of Triple Shiftian.
    :param num: int : sequence number, we want to finds value of.
    :return: int : value of n-th element from Triple Shiftian.
    """
    shiftian = first_three_elements[:]
    for i in range(2, num):
        item = 4 * shiftian[i] - 5 * shiftian[i - 1] + 3 * shiftian[i - 2]
        shiftian.append(item)
    return shiftian[-1]


def sum_of_square(line_number: int) -> int:
    """
    Calculate the sum of the squares of the binomial coefficients
    :param line_number : int : the line number
    :returns : int : the sum of the squares of the binomial coefficients on line n.
    """

    pascal_triangle = [[0 for i in range(line_number + 1)]for j in range(line_number + 1)]
    for i in range(0, line_number + 1):

        for j in range(0, min(i, line_number) + 1):
            if (j == 0 or i == 0):
                pascal_triangle[i][j] = 1
            else:
                pascal_triangle[i][j] = (pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])

    result = 0
    for i in range(0, line_number+1):
        result += pow(pascal_triangle[line_number][i], 2)
    return result


def sequence_sum(begin_number, end_number, step):
    """
    Calculates sum of sequence
    :param begin_number: int : start of sequence
    :param end_number: int : end of sequence
    :param step: int : step
    :return: int : sum of sequence
    """
    return sum(list(range(begin_number, end_number+1, step)))


def replicate(times, number):
    """
    Function should return list containing repetitions of the number argument
    :param: times: int : number of repetitions
    :param: number: int : number that repeats
    :return: arr list : list.
    """
    if times <= 0:
        return []
    if times == 1:
        return [number]
    list_of_nums = [number]
    return list_of_nums + replicate(times-1, number)


def where_is_vasya(total, in_front):
    """Vasya stands in line with number of people p (including Vasya),
    but he doesn't know exactly which position he occupies.
    He can say that there are no less than b people standing in front of him
    and no more than a people standing behind him.
    Find the number of different positions Vasya can occupy.

    :param total: int : Total amount of people in the line.
    :param in_front: int : Number of people standing in front of him (no less than).

    :return: int: Number of possible positions.

    """
    positions = total - in_front

    return positions


def new_avg(arr, navg):
    """
    Function find expected number that will permit to reach the average navg.
    :param arr: list : array of numbers.
    :param navg: int : expected average.
    :return: int : positive number.
    :raise: ValueError : if 'num' is negative.
    """
    num = navg*(len(arr)+1) - sum(arr)
    if num < 0:
        raise ValueError

    return ceil(num)
