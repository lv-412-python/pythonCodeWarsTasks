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
121 Gasoline;! 13.6?;""",  """Original Balance: 1233.00\r
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
