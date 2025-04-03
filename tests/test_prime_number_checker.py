import pytest
from src.prime_number_checker import is_prime

def test_prime_numbers():
    """Test known prime numbers."""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
                     997, 991, 983, 977, 971]
    for prime in prime_numbers:
        assert is_prime(prime) is True, f"{prime} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers."""
    non_prime_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 
                         20, 21, 22, 24, 25, 26, 27, 28, 
                         989, 990, 992, 993, 994, 995, 996, 998, 999, 1000]
    for non_prime in non_prime_numbers:
        assert is_prime(non_prime) is False, f"{non_prime} should not be prime"

def test_input_validation():
    """Test input validation for the is_prime function."""
    # Test lower bound
    with pytest.raises(ValueError, match="Input must be between 2 and 1000"):
        is_prime(1)
    
    # Test upper bound
    with pytest.raises(ValueError, match="Input must be between 2 and 1000"):
        is_prime(1001)
    
    # Test non-integer input
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime(3.14)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime("17")