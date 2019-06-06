"""Tests for 6kyu module"""

import pytest
from tasks.kyu6 import (
    interp,
    approximation,
    bouncing_ball,
    nba_cup, R,
    variance_rainfall, DATA,
    balance,
    consonant_value,
    find_nb
)


@pytest.mark.parametrize('height, bounce, expected_output', [
    (3, 0.66, 3),
    (30, 0.66, 15),
    ])
def test_bouncing_ball(height, bounce, expected_output):
    """Tests bouncing_ball function"""
    result = bouncing_ball(height, bounce)
    assert result == expected_output
    with pytest.raises(TypeError) as err:
        assert bouncing_ball('string', 'second string') is err


@pytest.mark.parametrize('result_sheet, to_find, expected_output',
                         [
                             (R, "Boston Celtics",
                              "Boston Celtics:W=4;D=0;L=0;Scored=403;Conceded=350;Points=12"),
                             (R, "Boston Celt",
                              "Boston Celt:This team didn't play!")
                         ])
def test_nba_cup(result_sheet, to_find, expected_output):
    """Tests nba_cup function"""
    result = nba_cup(result_sheet, to_find)
    assert result == expected_output
    with pytest.raises(AttributeError) as attr_error:
        assert nba_cup(2, 1) is attr_error



@pytest.mark.parametrize('string, expected_output',
                         [
                             ("zodiac", 26),
                             ("chruschtschov", 80),
                             ("khrushchev", 38),
                             ("strength", 57),
                             ("catchphrase", 73),
                             ("twelfthstreet", 103),
                             ("mischtschenkoana", 80)
                         ])
def test_consonant_value(string, expected_output):
    """Tests consonant_value function."""
    result = consonant_value(string)
    assert result == expected_output


STRINGS_FOR_BALANCE = [("""1000.00!=

125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.10
""", """Original Balance: 1000.00\r
125 Market 125.45 Balance 874.55\r
126 Hardware 34.95 Balance 839.60\r
127 Video 7.45 Balance 832.15\r
128 Book 14.32 Balance 817.83\r
129 Gasoline 16.10 Balance 801.73\r
Total expense  198.27\r
Average expense  39.65"""), ("""1233.00
125 Hardware;! 24.8?;
123 Flowers 93.5
127 Meat 120.90
120 Picture 34.00
124 Gasoline 11.00
123 Photos;! 71.4?;
122 Picture 93.5
132 Tyres;! 19.00,?;
129 Stamps 13.6
129 Fruits{} 17.6
129 Market;! 128.00?;
121 Gasoline;! 13.6?;""", """Original Balance: 1233.00\r
125 Hardware 24.80 Balance 1208.20\r
123 Flowers 93.50 Balance 1114.70\r
127 Meat 120.90 Balance 993.80\r
120 Picture 34.00 Balance 959.80\r
124 Gasoline 11.00 Balance 948.80\r
123 Photos 71.40 Balance 877.40\r
122 Picture 93.50 Balance 783.90\r
132 Tyres 19.00 Balance 764.90\r
129 Stamps 13.60 Balance 751.30\r
129 Fruits 17.60 Balance 733.70\r
129 Market 128.00 Balance 605.70\r
121 Gasoline 13.60 Balance 592.10\r
Total expense  640.90\r
Average expense  53.41""")]


@pytest.mark.parametrize("parameter", STRINGS_FOR_BALANCE)
def test_balance(parameter):
    """Tests balance function"""
    string, result = parameter
    assert balance(string) == result


def test_find_nb():
    """Tests find_nb function"""
    assert find_nb(4183059834009) == 2022
    assert find_nb(24723578342962) == -1
    assert find_nb(135440716410000) == 4824
    assert find_nb(40539911473216) == 3568
    assert find_nb(26825883955641) == 3218
    assert find_nb(0) == 0
    with pytest.raises(TypeError) as type_err:
        assert find_nb('a') is type_err


@pytest.mark.parametrize('city, strng, expected_output', [
    ("London", DATA, 57.42833333333374),
    ("Beijing", DATA, 4808.37138888889)],
                         ids=["['London', data]_57.42833333333374",
                              "['Beijing', data]_4808.37138888889)"])
def test_variance_rainfall(city, strng, expected_output):
    """Tests variance_rainfall function."""
    result = variance_rainfall(city, strng)
    assert pytest.approx(result, 1e-6) == expected_output
    with pytest.raises(AttributeError) as attr_err:
        assert variance_rainfall((1, 1), (2,3)) is attr_err


@pytest.mark.parametrize('data', [
    (2.6e-08, 1.2999999915500002e-08),
    (1.4e-09, 6.999999997549999e-10),
    (5.0e-06, 2.499996875007813e-06),
    (2.4e-07, 1.1999999280000087e-07)
    ])
def test_approximation(data):
    '''Tests approximation function'''
    num, result = data
    assert approximation(num) == result
    with pytest.raises(TypeError) as type_err:
        assert approximation((1, 2)) is type_err
