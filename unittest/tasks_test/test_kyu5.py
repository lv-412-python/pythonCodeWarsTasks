"""Tests for 5kyu module"""

import pytest
from tasks.kyu5 import fib_product
@pytest.mark.parametrize('product, expected_output', [
    (4895, [55, 89, True]),
    (5895, [89, 144, False]),
    ])
def test_fib_product(product, expected_output):
    """Test fib_product function"""
    result = fib_product(product)
    assert result == expected_output
