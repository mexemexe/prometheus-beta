import pytest
from src.count_matching_elements import count_matching_elements

def test_basic_matching():
    """Test basic matching of elements"""
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    assert count_matching_elements(arr1, arr2) == 3

def test_no_matching_elements():
    """Test case with no matching elements"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert count_matching_elements(arr1, arr2) == 0

def test_all_matching_elements():
    """Test case where all elements match"""
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3, 4, 5]
    assert count_matching_elements(arr1, arr2) == 3

def test_empty_arrays():
    """Test case with empty arrays"""
    arr1 = []
    arr2 = [1, 2, 3]
    assert count_matching_elements(arr1, arr2) == 0
    assert count_matching_elements(arr2, arr1) == 0

def test_duplicate_elements():
    """Test case with duplicate elements"""
    arr1 = [1, 1, 2, 2, 3]
    arr2 = [1, 2, 3, 3, 4]
    assert count_matching_elements(arr1, arr2) == 5

def test_invalid_input_non_list():
    """Test error handling for non-list inputs"""
    with pytest.raises(TypeError, match="Both inputs must be lists"):
        count_matching_elements("not a list", [1, 2, 3])
    with pytest.raises(TypeError, match="Both inputs must be lists"):
        count_matching_elements([1, 2, 3], "not a list")

def test_invalid_input_non_integers():
    """Test error handling for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        count_matching_elements([1, 2, "3"], [1, 2, 3])
    with pytest.raises(TypeError, match="All elements must be integers"):
        count_matching_elements([1, 2, 3], [1, 2, "3"])