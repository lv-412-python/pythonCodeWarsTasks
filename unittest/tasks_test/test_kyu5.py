"""Tests for 5kyu module"""

import pytest
from tasks.kyu5 import fib_product, zeros, prime_factors, smallest


@pytest.mark.parametrize('product, expected_output', [
    (4895, [55, 89, True]),
    (5895, [89, 144, False]),
    ])
def test_fib_product(product, expected_output):
    """Test fib_product function"""
    result = fib_product(product)
    assert result == expected_output


@pytest.mark.parametrize('num, expected_output',
                         [
                             (0, 0),
                             (6, 1),
                             (30, 7)
                         ])
def test_zeros(num, expected_output):
    """test zeros function"""
    result = zeros(num)
    assert result == expected_output


@pytest.mark.parametrize('number, expected_output',
                         [
                             (7775460, "(2**2)(3**3)(5)(7)(11**2)(17)"),

                         ])
def test_prime_factor(number, expected_output):
    """Test prime_factor function."""
    result = prime_factors(number)
    assert result == expected_output


@pytest.mark.parametrize("parameter",
                         [(261235, [126235, 2, 0]), (187863002809, [18786300289, 10, 0])])
def test_smallest(parameter):
    """Tests smallest function"""
    number, result = parameter
    assert smallest(number) == result
