"""Tests for 8kyu module"""

import pytest
from tasks.kyu8 import heads_legs
from tasks.kyu8 import short_long_short

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
    assert result == expected_output
