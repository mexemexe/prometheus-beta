def sum_of_multiples(limit, multiples):
    """
    Calculate the sum of all unique multiples of given numbers up to a limit.

    Args:
        limit (int): The upper bound (inclusive) for finding multiples.
        multiples (list): A list of integers to find multiples of.

    Returns:
        int: The sum of all unique multiples of numbers in the list up to the limit.

    Raises:
        ValueError: If limit or any number in multiples is less than or equal to 0.
    """
    # Validate inputs
    if limit <= 0:
        raise ValueError("Limit must be a positive integer.")
    
    if not multiples:
        return 0
    
    for multiple in multiples:
        if multiple <= 0:
            raise ValueError("All multiples must be positive integers.")
    
    # Use a set to track unique multiples
    unique_multiples = set()
    
    # Iterate through potential multiples
    for num in range(1, limit + 1):
        # Check if the number is a multiple of any number in the given list
        if any(num % m == 0 for m in multiples):
            unique_multiples.add(num)
    
    # Return the sum of unique multiples
    return sum(unique_multiples)