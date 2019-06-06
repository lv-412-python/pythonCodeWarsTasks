"""Tests for 6kyu module"""
import pytest
from tasks.kyu6 import bouncing_ball, nba_cup, R, consonant_value


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
