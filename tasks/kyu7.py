# -*- coding: utf-8 -*-
"""
    Task solution:
   https://www.codewars.com/kata/easy-line
"""

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
    Calculate sum of sequence
    :param begin_number: int : start of sequence
    :param end_number: int : end of sequence
    :param step: int : step
    :return: int : sum of sequence
    """
    return sum(list(range(begin_number, end_number+1, step)))
    