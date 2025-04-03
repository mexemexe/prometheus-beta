import pytest
from src.bubble_sort import bubble_sort

def test_basic_sorting():
    """Test basic sorting of a random list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    result = bubble_sort(arr)
    assert result == sorted(arr)

def test_already_sorted_list():
    """Test that an already sorted list remains unchanged."""
    arr = [1, 2, 3, 4, 5]
    result = bubble_sort(arr)
    assert result == arr

def test_reverse_sorted_list():
    """Test sorting a list in reverse order."""
    arr = [5, 4, 3, 2, 1]
    result = bubble_sort(arr)
    assert result == sorted(arr)

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    result = bubble_sort(arr)
    assert result == sorted(arr)

def test_empty_list():
    """Test sorting an empty list."""
    arr = []
    result = bubble_sort(arr)
    assert result == []

def test_single_element_list():
    """Test sorting a list with a single element."""
    arr = [42]
    result = bubble_sort(arr)
    assert result == arr

def test_type_error():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        bubble_sort("not a list")
    with pytest.raises(TypeError):
        bubble_sort(123)

def test_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-4, 1, -9, 0, 5, -2]
    result = bubble_sort(arr)
    assert result == sorted(arr)

def test_large_list():
    """Test sorting a relatively large list."""
    import random
    arr = [random.randint(-1000, 1000) for _ in range(500)]
    result = bubble_sort(arr)
    assert result == sorted(arr)