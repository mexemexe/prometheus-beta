import pytest
from src.first_occurrence_binary_search import find_first_occurrence

def test_basic_find_first_occurrence():
    """Test finding the first occurrence in a basic scenario"""
    arr = [1, 2, 2, 2, 3, 4, 5]
    assert find_first_occurrence(arr, 2) == 1

def test_find_first_occurrence_single_element():
    """Test finding first occurrence in a single-element array"""
    arr = [5]
    assert find_first_occurrence(arr, 5) == 0

def test_target_not_in_array():
    """Test when target is not in the array"""
    arr = [1, 3, 5, 7, 9]
    assert find_first_occurrence(arr, 4) == -1

def test_empty_array():
    """Test with an empty array"""
    arr = []
    assert find_first_occurrence(arr, 5) == -1

def test_target_at_start():
    """Test when target is at the start of the array"""
    arr = [1, 1, 2, 3, 4, 5]
    assert find_first_occurrence(arr, 1) == 0

def test_target_at_end():
    """Test when target is at the end of the array"""
    arr = [1, 2, 3, 4, 5, 5]
    assert find_first_occurrence(arr, 5) == 4

def test_invalid_input_non_list():
    """Test invalid input - non-list"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_first_occurrence("not a list", 5)

def test_invalid_input_non_integer_target():
    """Test invalid input - non-integer target"""
    with pytest.raises(TypeError, match="Target must be an integer"):
        find_first_occurrence([1, 2, 3], "5")

def test_invalid_input_non_positive_integers():
    """Test invalid input - array with non-positive integers"""
    with pytest.raises(ValueError, match="Array must contain only positive integers"):
        find_first_occurrence([1, -2, 3], 2)
    with pytest.raises(ValueError, match="Array must contain only positive integers"):
        find_first_occurrence([1, 2.5, 3], 2)