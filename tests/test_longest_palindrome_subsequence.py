import pytest
from src.longest_palindrome_subsequence import longest_palindrome_subsequence

def test_empty_string():
    """Test that an empty string returns 0"""
    assert longest_palindrome_subsequence("") == 0

def test_single_character():
    """Test that a single character returns 1"""
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("z") == 1

def test_two_identical_characters():
    """Test that two identical characters return 2"""
    assert longest_palindrome_subsequence("aa") == 2
    assert longest_palindrome_subsequence("bb") == 2

def test_basic_palindrome_subsequences():
    """Test various palindrome subsequence scenarios"""
    assert longest_palindrome_subsequence("bbbab") == 4  # "bbbb"
    assert longest_palindrome_subsequence("cbbd") == 2   # "bb"

def test_complex_palindrome_subsequences():
    """Test more complex palindrome subsequence scenarios"""
    assert longest_palindrome_subsequence("abcdef") == 1  # only single character subsequences
    assert longest_palindrome_subsequence("racecar") == 7  # entire string is a palindrome
    assert longest_palindrome_subsequence("aabaa") == 5  # entire string is a palindrome

def test_mixed_characters():
    """Test palindrome subsequences with mixed characters"""
    assert longest_palindrome_subsequence("forgeeksskeegfor") == 12  # full "forgeeksskeegfor" is a palindrome
    assert longest_palindrome_subsequence("abcda") == 3  # "aca"

def test_repeated_characters():
    """Test strings with many repeated characters"""
    assert longest_palindrome_subsequence("aaaaaa") == 6  # entire string is a palindrome
    assert longest_palindrome_subsequence("abcccccccccccba") == 15  # entire string is a palindrome