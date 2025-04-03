def is_prime(n: int) -> bool:
    """
    Determine whether an input integer is a prime number.

    A prime number is a natural number greater than 1 that is only divisible by 1 and itself.

    Args:
        n (int): The number to check for primality.
               Must be an integer between 2 and 1000 (inclusive).

    Returns:
        bool: True if the number is prime, False otherwise.

    Raises:
        ValueError: If the input is not an integer between 2 and 1000.
    """
    # Validate input range
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n < 2 or n > 1000:
        raise ValueError("Input must be between 2 and 1000")
    
    # Check for primality using trial division
    # We only need to check up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True