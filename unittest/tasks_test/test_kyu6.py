"""Tests for 6kyu module"""
import pytest
from tasks.kyu6 import bouncing_ball, nba_cup, R, consonant_value, balance


@pytest.mark.parametrize('height, bounce, expected_output', [
    (3, 0.66, 3),
    (30, 0.66, 15),
    ])
def test_bouncing_ball(height, bounce, expected_output):
    """Test bouncing_ball function"""
    result = bouncing_ball(height, bounce)
    assert result == expected_output


@pytest.mark.parametrize('result_sheet, to_find, expected_output',
                         [
                             (R, "Boston Celtics",
                              "Boston Celtics:W=4;    D=0;    L=0;    Scored=403;\
    Conceded=350;    Points=12"),
                             (R, "Boston Celt",
                              "Boston Celt:This team didn't play!")
                         ])
def test_nba_cup(result_sheet, to_find, expected_output):
    result = nba_cup(result_sheet, to_find)
    assert result == expected_output


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
    """Test consonant_value function."""
    result = consonant_value(string)
    assert result == expected_output


STRINGS_FOR_BALANCE = [("""1242.00
122 Hardware;! 13.6
127 Hairdresser 13.1
123 Fruits 93.5?;
132 Stamps;!{ 13.6?;
160 Pen;! 17.6?;
002 Car;! 34.00""", "Original Balance: 1242.00\n122 Hardware 13.60 Balance 1228.40\n127 Hairdresser\
 13.10 Balance 1215.30\n123 Fruits 93.50 Balance 1121.80\n132 Stamps 13.60 Balance 1108.20\n160 Pen 17.60 \
 Balance 1090.60\n002 Car 34.00 Balance 1056.60\nTotal expense  185.40\nAverage expense  30.90"),
                       ("""963.0
131 Books 12.2
139 Gasoline 120.90
002 Hardware;! 71.4?;""", "Original Balance: 963.00\n131 Books \
 12.20 Balance 950.80\n139 Gasoline 120.90 Balance 829.90\n002 Hardware 71.40 Balance 758.50\nTotal expense  204.50\n\
 Average expense  68.17")]


@pytest.mark.parametrize("parameter", STRINGS_FOR_BALANCE)
def test_balance(parameter):
    """Tests balance function"""
    string, result = parameter
    assert balance(string) == result
