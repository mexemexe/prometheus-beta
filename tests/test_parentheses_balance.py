import pytest
from src.parentheses_balance import is_balanced_parentheses

def test_empty_string():
    """Test empty string is considered balanced."""
    assert is_balanced_parentheses("") == True

def test_simple_balanced():
    """Test simple balanced parentheses."""
    assert is_balanced_parentheses("()") == True
    assert is_balanced_parentheses("(())") == True
    assert is_balanced_parentheses("((()))") == True

def test_unbalanced_parentheses():
    """Test various unbalanced parentheses scenarios."""
    assert is_balanced_parentheses("(") == False
    assert is_balanced_parentheses(")") == False
    assert is_balanced_parentheses(")(") == False
    assert is_balanced_parentheses("((()") == False
    assert is_balanced_parentheses("())") == False

def test_multiple_balanced_groups():
    """Test multiple balanced parentheses groups."""
    assert is_balanced_parentheses("()()") == True
    assert is_balanced_parentheses("(())()") == True
    assert is_balanced_parentheses("((()()))") == True

def test_nested_balanced():
    """Test deeply nested balanced parentheses."""
    assert is_balanced_parentheses("(((())))") == True
    assert is_balanced_parentheses("(()()(()))") == True

def test_large_input():
    """Test balance with a large number of parentheses."""
    large_balanced = "(" * 1000 + ")" * 1000
    large_unbalanced = "(" * 1000 + ")" * 999
    
    assert is_balanced_parentheses(large_balanced) == True
    assert is_balanced_parentheses(large_unbalanced) == False