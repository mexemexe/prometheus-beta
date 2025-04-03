import pytest
from src.string_reverser import reverse_string_in_place

def test_reverse_normal_string():
    """Test reversing a normal string"""
    s = list('hello')
    reverse_string_in_place(s)
    assert s == list('olleh')

def test_reverse_single_character():
    """Test reversing a single character string"""
    s = list('a')
    reverse_string_in_place(s)
    assert s == list('a')

def test_reverse_empty_string():
    """Test reversing an empty string"""
    s = []
    reverse_string_in_place(s)
    assert s == []

def test_reverse_even_length_string():
    """Test reversing a string with even number of characters"""
    s = list('abcd')
    reverse_string_in_place(s)
    assert s == list('dcba')

def test_reverse_with_special_characters():
    """Test reversing a string with special characters"""
    s = list('a1b2c3')
    reverse_string_in_place(s)
    assert s == list('3c2b1a')

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of characters"):
        reverse_string_in_place("not a list")

def test_reverse_with_unicode():
    """Test reversing a string with Unicode characters"""
    s = list('こんにちは')
    reverse_string_in_place(s)
    assert s == list('はちにんこ')