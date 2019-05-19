
# -*- coding: utf-8 -*-
"""Task solution:
   https://www.codewars.com/kata/floating-point-approximation-ii
"""
from math import sin, cos, floor
import re

WINDOW = 1.5


def find_nb(volume):
    """
    Calculates the number of n cubes from building's volume

    :param volume : int : The volume of a building
    :return int: number of cubes
    """
    vol = 0
    amount = 1
    while vol != volume:
        vol += amount**3
        amount += 1
        if vol > volume:
            return -1
    return amount - 1


def bouncing_ball(height, bounce):
    """
    Finds how many times the ball will pass in front of the window (1.5 meters height),
    including falling and bouncing.
    :param height: float : the height of the floor.
    :param bounce: float : a bounce of the ball.
    :return: int : number of bounces or -1 in case when one of the conditions is not fulfilled.
    """

    bounce_num = 1

    if height > 0 and 0 < bounce < 1 and WINDOW < height:
        while bounce * height > WINDOW:
            bounce_num += 2
            height *= bounce
        return bounce_num

    return -1


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


def approximation(num):
    """
    give a good approximation of f(x) in the neigbourhood of 0?
    :param num: float : number
    :return: float : approximation of f(x) in the neigbourhood of 0
    """
    return num/2-num**2/8+num**3/16-5/128*num**4+7/256*num**5


R = ("Los Angeles Clippers 104 Dallas Mavericks 88,"
     "New York Knicks 101 Atlanta Hawks 112,"
     "Indiana Pacers 103 Memphis Grizzlies 112,"
     "Los Angeles Lakers 111 Minnesota Timberwolves 112,"
     "Phoenix Suns 95 Dallas Mavericks 111,"
     "Portland Trail Blazers 112 New Orleans Pelicans 94,"
     "Sacramento Kings 104 Los Angeles Clippers 111,"
     "Houston Rockets 85 Denver Nuggets 105,"
     "Memphis Grizzlies 76 Cleveland Cavaliers 106,"
     "Milwaukee Bucks 97 New York Knicks 122,"
     "Oklahoma City Thunder 112 San Antonio Spurs 106,"
     "Boston Celtics 112 Philadelphia 76ers 95,"
     "Brooklyn Nets 100 Chicago Bulls 115,"
     "Detroit Pistons 92 Utah Jazz 87,"
     "Miami Heat 104 Charlotte Hornets 94,"
     "Toronto Raptors 106 Indiana Pacers 99,"
     "Orlando Magic 87 Washington Wizards 88,"
     "Golden State Warriors 111 New Orleans Pelicans 95,"
     "Atlanta Hawks 94 Detroit Pistons 106,"
     "Chicago Bulls 97 Cleveland Cavaliers 95,"
     "San Antonio Spurs 111 Houston Rockets 86,"
     "Chicago Bulls 103 Dallas Mavericks 102,"
     "Minnesota Timberwolves 112 Milwaukee Bucks 108,"
     "New Orleans Pelicans 93 Miami Heat 90,"
     "Boston Celtics 81 Philadelphia 76ers 65,"
     "Detroit Pistons 115 Atlanta Hawks 87,"
     "Toronto Raptors 92 Washington Wizards 82,"
     "Orlando Magic 86 Memphis Grizzlies 76,"
     "Los Angeles Clippers 115 Portland Trail Blazers 109,"
     "Los Angeles Lakers 97 Golden State Warriors 136,"
     "Utah Jazz 98 Denver Nuggets 78,"
     "Boston Celtics 99 New York Knicks 85,"
     "Indiana Pacers 98 Charlotte Hornets 86,"
     "Dallas Mavericks 87 Phoenix Suns 99,"
     "Atlanta Hawks 81 Memphis Grizzlies 82,"
     "Miami Heat 110 Washington Wizards 105,"
     "Detroit Pistons 94 Charlotte Hornets 99,"
     "Orlando Magic 110 New Orleans Pelicans 107,"
     "Los Angeles Clippers 130 Golden State Warriors 95,"
     "Utah Jazz 102 Oklahoma City Thunder 113,"
     "San Antonio Spurs 84 Phoenix Suns 104,"
     "Chicago Bulls 103 Indiana Pacers 94,"
     "Milwaukee Bucks 106 Minnesota Timberwolves 88,"
     "Los Angeles Lakers 104 Portland Trail Blazers 102,"
     "Houston Rockets 120 New Orleans Pelicans 100,"
     "Boston Celtics 111 Brooklyn Nets 105,"
     "Charlotte Hornets 94 Chicago Bulls 86,"
     "Cleveland Cavaliers 103 Dallas Mavericks 97")


def nba_cup(result_sheet, to_find):
    """
    If the number has an integer square root, take this, otherwise square the number.
    :param: result_sheet: str : Matches and scores.
    :param: to_find: str : Name of the team.
    :return: str : Returns a string with team statistics.
    """
    if to_find == '':
        return ''
    result_sheet = result_sheet.lower()
    to_find = to_find.lower()
    wins = draws = losses = scored = conceded = points = 0
    for act in result_sheet.split(','):
        matched = re.search(r'^(.*?) (\d+) (.*?) (\d+)$', act)
        if not matched:
            return f'Error(float number):{act}'
        teams = {
            "f_team": '',
            "f_score": 0,
            "s_team": '',
            "s_score": 0
        }
        teams["f_team"], teams["f_score"], teams["s_team"], teams["s_score"] = matched.groups()
        first_score, second_score = int(teams["f_score"]), int(teams["s_score"])
        if teams["f_team"] == to_find:
            score, concede = first_score, second_score
        elif teams["s_team"] == to_find:
            score, concede = second_score, first_score
        else:
            continue
        scored += score
        conceded += concede
        if score > concede:
            wins += 1
            points += 3
        elif score < concede:
            losses += 1
            points += 0
        else:
            draws += 1
            points += 1
    if wins == draws == losses == 0:
        return f"{to_find}:This team didn't play!"
    return f'{to_find.title()}:W={wins};\
    D={draws};\
    L={losses};\
    Scored={scored};\
    Conceded={conceded};\
    Points={points}'
