# -*- coding: utf-8 -*-
"""Task solution:
   https://www.codewars.com/kata/floating-point-approximation-ii
"""
from math import sin, cos, floor

def interp(func: str, l_a: float, u_b: float, n_c: int) -> list:
    """Search for some intermediate results.
        :func : func or str : receive your function(sin or cos) or string.
        :l_a : float : some float number (0<=l).
        :u_b : float : some float number (l<u).
        :n_c : int : number of elements in res_list.
        :returns : list : list all of intermediate results where length = n.
    """
    if func == 'sin':
        func = sin
    elif func == 'cos':
        func = cos

    res_list = []
    if n_c < 3:
        return res_list

    if 0 <= l_a < u_b:
        res_list = [None]*n_c
        d_d = (u_b-l_a)/n_c

        if isinstance(func, str):
            res_list[0] = round_to_lower(l_a)
            res_list[1] = round_to_lower(l_a+d_d)
            res_list[-1] = round_to_lower(u_b-d_d)

            for i in range(2, n_c-1):
                res_list[i] = round_to_lower(d_d*i)

            return res_list

        res_list[0] = round_to_lower(func(l_a))
        res_list[1] = round_to_lower(func(l_a+d_d))
        res_list[-1] = round_to_lower(func(u_b-d_d))

        for i in range(2, n_c-1):
            res_list[i] = round_to_lower(func(d_d*i))

        return res_list
    return None

def round_to_lower(i: float) -> float:
    """
    Round down to a less value.
        :i : float : some intermediate results.
        :returns : float : round up to a smaller number.
    """
    return floor(i*100.0)/100.0
