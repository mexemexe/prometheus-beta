import pytest
from src.reverse_matrix_elements import reverse_matrix_elements

def test_basic_matrix_reversal():
    matrix = [
        [1, 23, 4],
        [56, 7, 89],
        [0, 12, 34]
    ]
    expected = [
        [1, 32, 4],
        [65, 7, 98],
        [0, 21, 43]
    ]
    assert reverse_matrix_elements(matrix) == expected

def test_single_element_matrix():
    matrix = [[5]]
    assert reverse_matrix_elements(matrix) == [[5]]

def test_matrix_with_zeros():
    matrix = [
        [0, 1, 2],
        [3, 0, 5],
        [6, 7, 0]
    ]
    expected = [
        [0, 1, 2],
        [3, 0, 5],
        [6, 7, 0]
    ]
    assert reverse_matrix_elements(matrix) == expected

def test_invalid_matrix_size():
    with pytest.raises(ValueError, match="Matrix must be square"):
        reverse_matrix_elements([[1, 2], [3, 4, 5]])

def test_matrix_out_of_range_elements():
    with pytest.raises(ValueError, match="Matrix elements must be in range"):
        reverse_matrix_elements([[1, 2], [10, 3]])

def test_matrix_size_constraints():
    with pytest.raises(ValueError, match="Matrix size must be between 1 and 1000"):
        reverse_matrix_elements([[] for _ in range(1001)])

def test_large_matrix_reversal():
    # Test a larger matrix to ensure performance and correctness
    matrix = [
        [12, 34, 56, 78],
        [90, 11, 22, 33],
        [44, 55, 66, 77],
        [88, 99, 0, 1]
    ]
    expected = [
        [21, 43, 65, 87],
        [09, 11, 22, 33],
        [44, 55, 66, 77],
        [88, 99, 0, 1]
    ]
    assert reverse_matrix_elements(matrix) == expected