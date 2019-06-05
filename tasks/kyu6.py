# -*- coding: utf-8 -*-
"""Task solution:
   https://www.codewars.com/kata/floating-point-approximation-ii
"""
from math import sin, cos, floor
import re

WINDOW = 1.5
VALUES_FOR_CHARS = dict(zip(
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
     'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], [i for i in range(1, 27)]))

DATA = ("Rome:Jan 81.2,Feb 63.2,Mar 70.3,Apr 55.7,May 53.0,Jun 36.4,Jul 17.5,"
        "Aug 27.5,Sep 60.9,Oct 117.7,Nov 111.0,Dec 97.9\n"
        "London:Jan 48.0,Feb 38.9,Mar 39.9,Apr 42.2,May 47.3,Jun 52.1,Jul 59.5,"
        "Aug 57.2,Sep 55.4,Oct 62.0,Nov 59.0,Dec 52.9\n"
        "Paris:Jan 182.3,Feb 120.6,Mar 158.1,Apr 204.9,May 323.1,Jun 300.5,"
        "Jul 236.8,Aug 192.9,Sep 66.3,Oct 63.3,Nov 83.2,Dec 154.7\n"
        "NY:Jan 108.7,Feb 101.8,Mar 131.9,Apr 93.5,May 98.8,Jun 93.6,Jul 102.2,"
        "Aug 131.8,Sep 92.0,Oct 82.3,Nov 107.8,Dec 94.2\n"
        "Vancouver:Jan 145.7,Feb 121.4,Mar 102.3,Apr 69.2,May 55.8,Jun 47.1,"
        "Jul 31.3,Aug 37.0,Sep 59.6,Oct 116.3,Nov 154.6,Dec 171.5\n"
        "Sydney:Jan 103.4,Feb 111.0,Mar 131.3,Apr 129.7,May 123.0,Jun 129.2,"
        "Jul 102.8,Aug 80.3,Sep 69.3,Oct 82.6,Nov 81.4,Dec 78.2\n"
        "Bangkok:Jan 10.6,Feb 28.2,Mar 30.7,Apr 71.8,May 189.4,Jun 151.7,"
        "Jul 158.2,Aug 187.0,Sep 319.9,Oct 230.8,Nov 57.3,Dec 9.4\n"
        "Tokyo:Jan 49.9,Feb 71.5,Mar 106.4,Apr 129.2,May 144.0,Jun 176.0,"
        "Jul 135.6,Aug 148.5,Sep 216.4,Oct 194.1,Nov 95.6,Dec 54.4\n"
        "Beijing:Jan 3.9,Feb 4.7,Mar 8.2,Apr 18.4,May 33.0,Jun 78.1,Jul 224.3,"
        "Aug 170.0,Sep 58.4,Oct 18.0,Nov 9.3,Dec 2.7\n"
        "Lima:Jan 1.2,Feb 0.9,Mar 0.7,Apr 0.4,May 0.6,Jun 1.8,Jul 4.4,Aug 3.1,"
        "Sep 3.3,Oct 1.7,Nov 0.5,Dec 0.7\n")

DATA1 = ("Rome:Jan 90.2,Feb 73.2,Mar 80.3,Apr 55.7,May 53.0,Jun 36.4,Jul 17.5,"
         "Aug 27.5,Sep 60.9,Oct 147.7,Nov 121.0,Dec 97.9\n"
         "London:Jan 58.0,Feb 38.9,Mar 49.9,Apr 42.2,May 67.3,Jun 52.1,"
         "Jul 59.5,Aug 77.2,Sep 55.4,Oct 62.0,Nov 69.0,Dec 52.9\n"
         "Paris:Jan 182.3,Feb 120.6,Mar 188.1,Apr 204.9,May 323.1,Jun 350.5,"
         "Jul 336.8,Aug 192.9,Sep 66.3,Oct 63.3,Nov 83.2,Dec 154.7\n"
         "NY:Jan 128.7,Feb 121.8,Mar 151.9,Apr 93.5,May 98.8,Jun 93.6,"
         "Jul 142.2,Aug 131.8,Sep 92.0,Oct 82.3,Nov 107.8,Dec 94.2\n"
         "Vancouver:Jan 155.7,Feb 121.4,Mar 132.3,Apr 69.2,May 85.8,Jun 47.1,"
         "Jul 31.3,Aug 37.0,Sep 69.6,Oct 116.3,Nov 154.6,Dec 171.5\n"
         "Sydney:Jan 123.4,Feb 111.0,Mar 151.3,Apr 129.7,May 123.0,Jun 159.2,"
         "Jul 102.8,Aug 90.3,Sep 69.3,Oct 82.6,Nov 81.4,Dec 78.2\n"
         "Bangkok:Jan 20.6,Feb 28.2,Mar 40.7,Apr 81.8,May 189.4,Jun 151.7,"
         "Jul 198.2,Aug 197.0,Sep 319.9,Oct 230.8,Nov 57.3,Dec 9.4\n"
         "Tokyo:Jan 59.9,Feb 81.5,Mar 106.4,Apr 139.2,May 144.0,Jun 186.0,"
         "Jul 155.6,Aug 148.5,Sep 216.4,Oct 194.1,Nov 95.6,Dec 54.4\n"
         "Beijing:Jan 13.9,Feb 14.7,Mar 18.2,Apr 18.4,May 43.0,Jun 88.1,"
         "Jul 224.3,Aug 170.0,Sep 58.4,Oct 38.0,Nov 19.3,Dec 2.7\n"
         "Lima:Jan 11.2,Feb 10.9,Mar 10.7,Apr 10.4,May 10.6,Jun 11.8,Jul 14.4,"
         "Aug 13.1,Sep 23.3,Oct 1.7,Nov 0.5,Dec 10.7\n")

TOWNS = ["Rome", "London", "Paris", "NY", "Vancouver", "Sydney", "Bangkok", "Tokyo",
         "Beijing", "Lima", "Montevideo", "Caracas", "Madrid", "Berlin"]

def find_nb(volume):
    """
    Calculates the number of n cubes from building's volume

    :param volume : int : The volume of a building
    :return int: number of cubes
    """
    vol = 0
    amount = 1
    while vol != volume:
        vol += amount ** 3
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
        res_list = [None] * n_c
        d_d = (u_b - l_a) / n_c

        if isinstance(func, str):
            res_list[0] = round_to_lower(l_a)
            res_list[1] = round_to_lower(l_a + d_d)
            res_list[-1] = round_to_lower(u_b - d_d)

            for i in range(2, n_c - 1):
                res_list[i] = round_to_lower(d_d * i)

            return res_list

        res_list[0] = round_to_lower(func(l_a))
        res_list[1] = round_to_lower(func(l_a + d_d))
        res_list[-1] = round_to_lower(func(u_b - d_d))

        for i in range(2, n_c - 1):
            res_list[i] = round_to_lower(func(d_d * i))

        return res_list
    return None


def round_to_lower(i: float) -> float:
    """
    Round down to a less value.
        :i : float : some intermediate results.
        :returns : float : round up to a smaller number.
    """
    return floor(i * 100.0) / 100.0


def approximation(num):
    """
    give a good approximation of f(x) in the neigbourhood of 0?
    :param num: float : number
    :return: float : approximation of f(x) in the neigbourhood of 0
    """
    return num / 2 - num ** 2 / 8 + num ** 3 / 16 - 5 / 128 * num ** 4 + 7 / 256 * num ** 5


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
    Function gets name of the team and print statistic of this team.
    :param result_sheet: str : Matches and scores.
    :param to_find: str : Name of the team.
    :return: str : Returns a string with team statistics.
    """
    if to_find == '':
        return ''
    result_sheet = result_sheet.lower()
    to_find = to_find.lower()
    wins = draws = losses = scored = conceded = points = 0
    for game in result_sheet.split(','):
        matched = re.search(r'^(.*?) (\d+) (.*?) (\d+)$', game)
        if not matched:
            return f'Error(float number):{game.title()}'
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
        return f"{to_find.title()}:This team didn't play!"
    if to_find.split(' ')[1] == "76ers":
        to_find = 'Philadelphia 76ers'
    else:
        to_find = to_find.title()
    return (f'{to_find}:W={wins};'
            f'D={draws};'
            f'L={losses};'
            f'Scored={scored};'
            f'Conceded={conceded};'
            f'Points={points}')


def mean_rainfall(town, strng):
    """Calculate mean value of rainfall in the city.

    :param town: str : Name of the location.
    :param strng: str : String with rainfall records for months from January to December.
    The records of towns are separated by \\n. The name of each town is followed by :.

    :return: float : Mean value of rainfall.

    """
    result = 0
    if not strng or strng.find(town + ':') == -1:
        result = -1
    else:
        data_r = strng.split('\n')
        avr = 0.0
        for i in data_r:
            if i.find(town) != -1:
                avr = [float(j) for j in re.findall(r'-?\d+\.?\d*', i)]
                avr = sum(avr) / 12
                break
        result = avr
    return result


def variance_rainfall(town, strng):
    """Calculate variance of rainfall in the city.

    :param town: str : Name of the location.
    :param strng: str : String with rainfall records for months from January to December.
    The records of towns are separated by \\n. The name of each town is followed by :.

    :return: float: Variance of rainfall.

    """
    result = 0
    if not strng or strng.find(town + ':') == -1:
        result = -1
    else:
        data_r = strng.split('\n')
        tmp = 0.0
        for i in data_r:
            if i.find(town) != -1:
                tmp = [float(j) for j in re.findall(r'-?\d+\.?\d*', i)]
                for value in tmp:
                    result += pow(value - mean_rainfall(town, strng), 2)
                result /= 12
                break
    return result


def balance(book):
    """
        Function clean the lines keeping only letters, digits, dots and spaces.
        Then add the new balance and then in the last two lines the total expense and
        the average expense.
        :param book: str : not formatted string.
        :return: str : formatted string(book).
    """
    book = ''.join([i for i in book if i not in '!:=?;,{}'])
    lst = [i for i in book.split('\n') if i]
    balance_ = float(lst[0])
    lst[0] = f"Original Balance: {balance_:.2f}\r\n"
    sum_ = 0
    for i in range(1, len(lst)):
        price = float(lst[i].split()[-1])
        sum_ += float(price)
        balance_ = balance_ - price
        lst[i] = ' '.join(lst[i].split()[0:-1]) + f" {price:.2f} Balance {balance_:.2f}\r\n"
    avg = sum_ / (len(lst) - 1)
    lst.append(f"Total expense  {sum_:.2f}\r\nAverage expense  {avg:.2f}")
    return ''.join(lst)


def consonant_value(string):
    """Return the highest value of consonant substrings
        :string : str : initial lowercase string
        :returns : int :  the highest value of consonant substrings
    """
    sub_val = []
    # Split string into substrings on vowels
    string = string.lower()

    string = re.sub('[aeiou]', ' ', string)
    substrings = string.split(' ')

    # Finds value of each substring
    for val in substrings:
        value = 0
        for j in val:
            if j in VALUES_FOR_CHARS:
                value += VALUES_FOR_CHARS[j]
            sub_val.append(value)
    return max(sub_val)
