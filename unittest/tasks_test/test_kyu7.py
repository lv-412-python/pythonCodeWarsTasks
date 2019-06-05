"""Tests for 7kyu module"""
import pytest

from tasks.kyu7 import triple_shiftian
@pytest.mark.parametrize('first_three_elements,num,expected_output', [
    ([1, 1, 1], 25, 1219856746),
    ([1, 2, 3], 25, 2052198929),
    ([6, 7, 2], 25, -2575238999),
    ([6, 7, 2], 2, 2)
    ])
def test_triple_shiftian(first_three_elements, num, expected_output):
    """Test triple_shiftian function"""
    result = triple_shiftian(first_three_elements, num)
    assert result == expected_output
