"""Tests for 7kyu module"""
import pytest

from tasks.kyu7 import (
    sum_of_square,
    sequence_sum,
    triple_shiftian,
    replicate,
    where_is_vasya,
    new_avg,
    angle,
    series_sum
)


@pytest.mark.parametrize('first_three_elements,num,expected_output', [
    ([1, 1, 1], 25, 1219856746),
    ([1, 2, 3], 25, 2052198929),
    ([6, 7, 2], 25, -2575238999),
    ([6, 7, 2], 2, 2)
    ])
def test_triple_shiftian(first_three_elements, num, expected_output):
    """Tests triple_shiftian function"""
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
    """Tests replicate function"""
    result = replicate(times, number)
    assert result == expected_output


@pytest.mark.parametrize('number, expected_result',
                         [
                             (3, 180),
                             (4, 360)
                         ])
def test_angle(number, expected_result):
    """Tests angle function."""
    result = angle(number)
    assert result == expected_result


def test_new_avg1():
    """Tests new_avg function"""
    assert new_avg([14, 30, 5, 7, 9, 11, 15], 92) == 645


def test_new_avg():
    """Tests new_avg function"""
    with pytest.raises(ValueError):
        new_avg([14, 30, 5, 7, 9, 11, 15], 2)


def test_series_sum():
    """Tests series_sum function """
    assert series_sum(1) == "1.00"
    assert series_sum(2) == "1.25"
    assert series_sum(3) == "1.39"
    assert series_sum(5) == "1.57"
    with pytest.raises(TypeError) as type_err:
        assert series_sum('a') is type_err
    assert series_sum(-5) == '1.00'


@pytest.mark.parametrize("people, bef, aft, expected_output", [
    (3, 1, 1, 2),
    (5, 2, 3, 3)],
                         ids=["(3, 1, 1)_2",
                              "(5, 2, 3)_3"])
def test_where_is_vasya(people, bef, aft, expected_output):
    """Tests where_is_vasya function."""
    result = where_is_vasya(people, bef, aft)
    assert result == expected_output
