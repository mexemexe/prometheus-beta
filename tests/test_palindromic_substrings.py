import pytest
from src.palindromic_substrings import find_palindromic_substrings

def test_basic_palindromes():
    """Test finding palindromic substrings in a simple string"""
    assert set(find_palindromic_substrings("abba")) == set(['a', 'b', 'bb', 'abba'])

def test_single_char_string():
    """Test a string with a single character"""
    assert set(find_palindromic_substrings("a")) == set(['a'])

def test_no_palindromes():
    """Test a string with no palindromes longer than single characters"""
    assert set(find_palindromic_substrings("abc")) == set(['a', 'b', 'c'])

def test_empty_string():
    """Test an empty string"""
    assert find_palindromic_substrings("") == []

def test_all_same_char():
    """Test a string with all the same characters"""
    result = find_palindromic_substrings("aaaa")
    assert set(result) == set(['a', 'aa', 'aaa', 'aaaa'])

def test_long_palindrome():
    """Test a longer palindromic string"""
    result = find_palindromic_substrings("racecar")
    expected = set(['r', 'a', 'c', 'e', 'racecar', 'aceca', 'cec'])
    assert set(result) == expected

def test_non_string_input():
    """Test handling of non-string input"""
    assert find_palindromic_substrings(None) == []
    assert find_palindromic_substrings(123) == []

def test_mixed_string():
    """Test a mixed string with multiple types of palindromes"""
    result = find_palindromic_substrings("madam")
    assert set(result) == set(['m', 'a', 'd', 'madam', 'ada'])

def test_output_sorted():
    """Verify that the output is sorted by length"""
    result = find_palindromic_substrings("abba")
    assert result == sorted(result, key=len)