import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_multiple():
    """Test basic multiple sum calculation."""
    assert sum_of_multiples(10, [3, 5]) == 23  # 3 + 5 + 6 + 9 + 10

def test_single_multiple():
    """Test with a single multiple."""
    assert sum_of_multiples(20, [7]) == 21  # 7 + 14

def test_no_multiples():
    """Test when no multiples exist."""
    assert sum_of_multiples(5, [11]) == 0

def test_empty_multiples_list():
    """Test with an empty multiples list."""
    assert sum_of_multiples(10, []) == 0

def test_large_limit():
    """Test with a larger limit."""
    assert sum_of_multiples(100, [3, 5]) == 2318  # Sum of multiples of 3 and 5 up to 100

def test_negative_limit_raises_error():
    """Test that a negative limit raises a ValueError."""
    with pytest.raises(ValueError, match="Limit must be a positive integer."):
        sum_of_multiples(-10, [3, 5])

def test_zero_limit_raises_error():
    """Test that a zero limit raises a ValueError."""
    with pytest.raises(ValueError, match="Limit must be a positive integer."):
        sum_of_multiples(0, [3, 5])

def test_negative_multiple_raises_error():
    """Test that a negative multiple raises a ValueError."""
    with pytest.raises(ValueError, match="All multiples must be positive integers."):
        sum_of_multiples(10, [3, -5])

def test_zero_multiple_raises_error():
    """Test that a zero multiple raises a ValueError."""
    with pytest.raises(ValueError, match="All multiples must be positive integers."):
        sum_of_multiples(10, [3, 0])

def test_duplicate_multiples():
    """Test that duplicate multiples are handled correctly."""
    assert sum_of_multiples(20, [3, 3, 5]) == 45  # Ensure only unique multiples are summed

def test_single_number_multiple():
    """Test with a single number multiple."""
    assert sum_of_multiples(10, [7]) == 7