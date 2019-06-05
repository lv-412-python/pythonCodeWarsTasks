"""Tests for 8kyu module"""

import pytest
from tasks.kyu8 import (
    short_long_short,
    litres,
    starting_mark,
    duty_free,
    validate_usr,
    fix_the_meerkat,
    square_or_square_root,
    heads_legs,
    volume_of_a_cuboid,
    miles_per_gallon_to_kilometers_per_liter,
    am_i_wilson,
    two_decimal_places,
    abbrev_name,
    bin_to_decimal,
    Circle,
    Point,
    circle_area,
    divisible_by
)


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
    """Test short_long_short function"""
    result = short_long_short(first, second)
    assert result == expected_output


@pytest.mark.parametrize('animal,expected_output',
                         [
                             (["tail", "body", "head"], ["head", "body", "tail"]),
                             (["bottom", "middle", "top"], ["top", "middle", "bottom"]),
                             (["ground", "rainbow", "sky"], ["sky", "rainbow", "ground"]),
                             (["tails", "body", "heads"], ["heads", "body", "tails"])
                         ])
def test_fix_the_meerkat(animal, expected_output):
    """ test fix_the_meerkat function"""
    result = fix_the_meerkat(animal)
    assert result == expected_output


@pytest.mark.parametrize('numbers, expected_output',
                         [
                             ([4, 3, 9, 7, 2, 1], [2, 9, 3, 49, 4, 1]),
                             ([100, 101, 5, 5, 1, 1], [10, 10201, 25, 25, 1, 1]),
                             ([1, 2, 3, 4, 5, 6], [1, 4, 9, 2, 25, 36])
                         ])
def test_square_or_square_root(numbers, expected_output):
    """ test square_or_square_root function"""
    result = square_or_square_root(numbers)
    assert result == expected_output


@pytest.mark.parametrize('name, abbrev',
                         [
                             ("Sam Harris", "S.H"),
                             ("Patrick Feenan", "P.F"),
                             ("Evan Cole", "E.C"),
                             ("P Favuzzi", "P.F"),
                             ("David Mendieta", "D.M")
                         ])
def test_abbrev_name(name, abbrev):
    """Test abbrev_name function."""
    result = abbrev_name(name)
    assert result == abbrev


@pytest.mark.parametrize('bin_n, decimal',
                         [
                             ("0", 0),
                             ("1", 1),
                             ("10", 2),
                             ("11", 3),
                             ("101010", 42),
                             ("1001001", 73)
                         ])
def test_bin_to_decimal(bin_n, decimal):
    """Test bin_to_decimal function."""
    result = bin_to_decimal(bin_n)
    assert result == decimal


@pytest.mark.parametrize("parameter", [(13, True), (563, True), (1, False)])
def test_am_i_wilson(parameter):
    """Tests am_i_wilson function"""
    number, result = parameter
    assert am_i_wilson(number) is result


@pytest.mark.parametrize("parameter", [(5.5589, 5.56), (3.3424, 3.34)])
def test_two_decimal_places(parameter):
    """Tests two_decimal_places function"""
    number, result = parameter
    assert two_decimal_places(number) == result

def test_divisible_by():
    assert divisible_by([1, 2, 3, 4, 5, 6], 1) == [1, 2, 3, 4, 5, 6]
    assert divisible_by([1, 2, 3, 4, 5, 6], 3) == [3, 6]
    assert divisible_by([0, 1, 2, 3, 4, 5, 6], 4), [0, 4]
    assert divisible_by([0], 4) == [0]
    assert divisible_by([1, 3, 5], 2) == []
    with pytest.raises(ZeroDivisionError) as zero_div:
        assert divisible_by([1, 2, 3, 4, 5, 6], 0) is zero_div
    with pytest.raises(NameError) as name_err:
        assert divisible_by([1, 2, 3, 4, 5, 6], a) is name_err

def test_circle_area():
    """Test circle_area function"""
    assert round(circle_area(Circle(Point(10, 10), 30)), 6) == 2827.433388
    assert round(circle_area(Circle(Point(25, -70), 30)), 6) == 2827.433388
    assert round(circle_area(Circle(Point(-15, 5), 0)), 6) == 0
    assert round(circle_area(Circle(Point(-15, 5), 12.5)), 6) == 490.873852
    with pytest.raises(TypeError) as type_err:
        assert circle_area('a') is type_err
