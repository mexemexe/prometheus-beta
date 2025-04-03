import pytest
from src.find_triplets import find_triplets_with_sum

def test_find_triplets_basic():
    # Basic case with multiple triplets
    arr = [1, 0, -1, 2, -2, 3]
    target_sum = 0
    expected = [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    result = find_triplets_with_sum(arr, target_sum)
    
    # Sort the results to compare regardless of order
    result = sorted(sorted(triplet) for triplet in result)
    expected = sorted(sorted(triplet) for triplet in expected)
    
    assert result == expected

def test_find_triplets_no_solution():
    # Case where no triplets sum to target
    arr = [1, 2, 3, 4, 5]
    target_sum = 100
    assert find_triplets_with_sum(arr, target_sum) == []

def test_find_triplets_duplicate_elements():
    # Case with duplicate elements
    arr = [-1, -1, 0, 1, 2, 2]
    target_sum = 2
    expected = [[-1, 0, 3], [-1, 1, 2]]
    result = find_triplets_with_sum(arr, target_sum)
    
    # Sort the results to compare regardless of order
    result = sorted(sorted(triplet) for triplet in result)
    expected = sorted(sorted(triplet) for triplet in expected)
    
    assert result == expected

def test_find_triplets_empty_list():
    # Empty list case
    arr = []
    target_sum = 0
    assert find_triplets_with_sum(arr, target_sum) == []

def test_find_triplets_invalid_input_type():
    # Invalid input type
    with pytest.raises(TypeError, match="Input must be a list"):
        find_triplets_with_sum("not a list", 0)

def test_find_triplets_invalid_target_sum_type():
    # Invalid target sum type
    with pytest.raises(TypeError, match="Target sum must be an integer"):
        find_triplets_with_sum([1, 2, 3], "not an integer")

def test_find_triplets_invalid_element_type():
    # Invalid element type in the list
    with pytest.raises(ValueError, match="All array elements must be integers"):
        find_triplets_with_sum([1, 2, "3"], 6)

def test_find_triplets_single_unique_solution():
    # Case with a single unique solution
    arr = [-1, 0, 1, 2, -1, -4]
    target_sum = 0
    expected = [[-1, -1, 2], [-1, 0, 1]]
    result = find_triplets_with_sum(arr, target_sum)
    
    # Sort the results to compare regardless of order
    result = sorted(sorted(triplet) for triplet in result)
    expected = sorted(sorted(triplet) for triplet in expected)
    
    assert result == expected