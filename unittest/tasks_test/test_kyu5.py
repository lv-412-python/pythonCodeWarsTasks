"""Tests for 5kyu module"""

import pytest
from tasks.kyu5 import (
    fib_product,
    moving_shift,
    demoving_shift,
    artificial_rain,
    zeros,
    gap_in_primes,
    smallest,
    prime_factors,
    solve
)


@pytest.mark.parametrize('product, expected_output', [
    (4895, [55, 89, True]),
    (5895, [89, 144, False]),
    ])
def test_fib_product(product, expected_output):
    """Tests fib_product function"""
    result = fib_product(product)
    assert result == expected_output


@pytest.mark.parametrize('num, expected_output',
                         [
                             (0, 0),
                             (6, 1),
                             (30, 7)
                         ])
def test_zeros(num, expected_output):
    """Tests zeros function"""
    result = zeros(num)
    assert result == expected_output


@pytest.mark.parametrize('number, expected_output',
                         [
                             (7775460, "(2**2)(3**3)(5)(7)(11**2)(17)"),

                         ])
def test_prime_factor(number, expected_output):
    """Tests prime_factor function."""
    result = prime_factors(number)
    assert result == expected_output


@pytest.mark.parametrize("parameter",
                         [(261235, [126235, 2, 0]), (187863002809, [18786300289, 10, 0])])
def test_smallest(parameter):
    """Tests smallest function"""
    number, result = parameter
    assert smallest(number) == result


def test_solve():
    """Tests solve function"""
    assert solve(2.00) == pytest.approx(5.000000000000e-01, 1e-12)
    assert solve(4.00) == pytest.approx(6.096117967978e-01, 1e-12)
    assert solve(5.00) == pytest.approx(6.417424305044e-01, 1e-12)
    assert solve(8.0) == pytest.approx(0.7034648345913732, 1e-12)
    with pytest.raises(TypeError) as type_err:
        assert solve('a') is type_err
    with pytest.raises(ZeroDivisionError) as zero_div:
        assert solve(0) is zero_div


@pytest.mark.parametrize("arg_list, expected_output", [
    ([2, 100, 110], [101, 103]),
    ([4, 100, 110], [103, 107]),
    ([8, 300, 400], [359, 367]),
    ([8, 300, 400], [359, 367]),
    ([10, 300, 400], [337, 347])],
                         ids=[
                             "(2, 100, 110)_[101, 103]",
                             "(4, 100, 110)_[103, 107]",
                             "(8, 300, 400)_[359, 367]",
                             "(8, 300, 400)_[359, 367]",
                             "(10, 300, 400)_[337, 347]"])
def test_gap_in_primes(arg_list, expected_output):
    """Tests gap_in_primes function."""
    result = gap_in_primes(arg_list[0], arg_list[1], arg_list[2])
    assert result == expected_output


def test_gap_in_primes_none():
    """Tests gap_in_primes function, when there's none output."""
    result = gap_in_primes(6, 100, 110)
    assert result is None
