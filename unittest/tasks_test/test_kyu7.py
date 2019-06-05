"""Tests for 7kyu module"""
import pytest

from tasks.kyu7 import triple_shiftian, replicate, angle, new_avg


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


@pytest.mark.parametrize('times, number, expected_output',
                         [
                             (3, 5, [5, 5, 5]),
                             (5, 1, [1, 1, 1, 1, 1]),
                             (0, 12, []),
                             (-1, 12, [])
                         ])
def test_replicate(times, number, expected_output):
    result = replicate(times, number)
    assert result == expected_output


@pytest.mark.parametrize('number, expected_result',
                         [
                             (3, 180),
                             (4, 360)
                         ])
def test_angle(number, expected_result):
    """Test angle function."""
    result = angle(number)
    assert result == expected_result


def test_new_avg1():
    """Tests new_avg function"""
    assert new_avg([14, 30, 5, 7, 9, 11, 15], 92) == 645


def test_new_avg():
    """Tests new_avg function"""
    with pytest.raises(ValueError):
        new_avg([14, 30, 5, 7, 9, 11, 15], 2)
