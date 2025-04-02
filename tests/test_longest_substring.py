import pytest
from src.longest_substring import find_longest_substring

def test_find_longest_substring_basic():
    """Test basic functionality of finding longest substring"""
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"

def test_find_longest_substring_edge_cases():
    """Test edge cases"""
    assert find_longest_substring("") == ""
    assert find_longest_substring("a") == "a"
    assert find_longest_substring("ab") == "ab"

def test_find_longest_substring_case_sensitivity():
    """Test case-sensitive behavior"""
    assert find_longest_substring("AbcA") == "Abc"
    assert find_longest_substring("aA") == "aA"

def test_find_longest_substring_complex_cases():
    """Test more complex substring scenarios"""
    assert find_longest_substring("dvdf") == "vdf"
    assert find_longest_substring("tmmzuxt") == "mzuxt"

def test_find_longest_substring_special_characters():
    """Test with special characters and mixed strings"""
    assert find_longest_substring("!@#$%^&*()") == "!@#$%^&*()"
    assert find_longest_substring("a1b2c3d4") == "a1b2c3d4"

def test_find_longest_substring_repeated_characters():
    """Test scenarios with repeated characters in different positions"""
    assert find_longest_substring("abcdefgabcdef") == "abcdefg"
    assert find_longest_substring("abccdefg") == "ccdefg"