import pytest
from src.unique_grid_paths import search_matrix

def test_search_matrix_target_present():
    """Test matrix search when target is present"""
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 9) == True
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 17) == True

def test_search_matrix_target_not_present():
    """Test matrix search when target is not present"""
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 2) == False
    assert search_matrix(matrix, 10) == False
    assert search_matrix(matrix, 100) == False

def test_search_matrix_single_element():
    """Test matrix search with a single-element matrix"""
    matrix = [[42]]
    assert search_matrix(matrix, 42) == True
    assert search_matrix(matrix, 43) == False

def test_search_matrix_rectangular():
    """Test matrix search with rectangular matrix"""
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    assert search_matrix(matrix, 4) == True
    assert search_matrix(matrix, 6) == True
    assert search_matrix(matrix, 7) == False

def test_search_matrix_invalid_input():
    """Test error handling for invalid matrix inputs"""
    with pytest.raises(ValueError, match="Matrix cannot be empty"):
        search_matrix([], 5)
    
    with pytest.raises(ValueError, match="Matrix cannot be empty"):
        search_matrix([[]], 5)
    
    with pytest.raises(ValueError, match="All rows must have the same length"):
        search_matrix([[1, 2], [3]], 5)