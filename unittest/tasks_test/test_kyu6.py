"""Tests for 6kyu module"""
import pytest
from tasks.kyu6 import bouncing_ball

@pytest.mark.parametrize('height, bounce, expected_output', [
    (3, 0.66, 3),
    (30, 0.66, 15),
    ])
def test_bouncing_ball(height, bounce, expected_output):
    """Test bouncing_ball function"""
    result = bouncing_ball(height, bounce)
    assert result == expected_output
