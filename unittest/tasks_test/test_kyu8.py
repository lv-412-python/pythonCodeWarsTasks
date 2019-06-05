"""Tests for 8kyu module"""

import pytest
from tasks.kyu8 import heads_legs
from tasks.kyu8 import short_long_short, fix_the_meerkat, square_or_square_root

@pytest.mark.parametrize('heads,legs,expected_output', [
    (72, 200, (44, 28)),
    (116, 282, (91, 25)),
    (12, 24, (12, 0)),
    (5, 5, "No solutions.")
    ])
def test_heads_legs(heads, legs, expected_output):
    """Test head_legs function"""
    result = heads_legs(heads, legs)
    assert result == expected_output


@pytest.mark.parametrize('first,second,expected_output', [
    ('45', '1', '1451'),
    ('13', '200', '1320013'),
    ('Soon', 'Me', 'MeSoonMe'),
    ('U', 'False', 'UFalseU')
    ])
def test_short_long_short(first, second, expected_output):
    """Test head_legs function"""
    result = short_long_short(first, second)


@pytest.mark.parametrize('animal,expected_output',
                         [
                             (["tail", "body", "head"], ["head", "body", "tail"]),
                             (["bottom", "middle", "top"], ["top", "middle", "bottom"]),
                             (["ground", "rainbow", "sky"], ["sky", "rainbow", "ground"]),
                             (["tails", "body", "heads"], ["heads", "body", "tails"])
                         ])
def test_heads_legs(animal, expected_output):
    result = fix_the_meerkat(animal)
    assert result == expected_output

@pytest.mark.parametrize('numbers, expected_output',
                         [
                             ([4, 3, 9, 7, 2, 1], [2, 9, 3, 49, 4, 1]),
                             ([100, 101, 5, 5, 1, 1], [10, 10201, 25, 25, 1, 1]),
                             ([1, 2, 3, 4, 5, 6], [1, 4, 9, 2, 25, 36])
                         ])
def test_square_or_square_root(numbers, expected_output):
    result = square_or_square_root(numbers)
    assert result == expected_output