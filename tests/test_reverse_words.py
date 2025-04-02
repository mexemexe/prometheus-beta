import pytest
from src.reverse_words import reverse_words

def test_basic_reverse():
    """Test basic word reversal."""
    assert reverse_words("Hello World") == "World Hello"

def test_multiple_spaces():
    """Test handling of multiple spaces between words."""
    assert reverse_words("  Hello   World  ") == "World Hello"

def test_alphanumeric_words():
    """Test words with non-alphabetic characters."""
    assert reverse_words("Hello123 World456") == "World456 Hello123"

def test_empty_string():
    """Test handling of empty string."""
    assert reverse_words("") == ""

def test_single_word():
    """Test handling of a single word."""
    assert reverse_words("Python") == "Python"

def test_multiple_words():
    """Test reversal of multiple words."""
    assert reverse_words("This is a test sentence") == "sentence test a is This"

def test_whitespace_only():
    """Test string with only whitespace."""
    assert reverse_words("   ") == ""