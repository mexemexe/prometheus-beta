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
    
    # Remove duplicates from the multiples list
    unique_multiples_list = list(set(multiples))
    
    # Use a set to track unique multiples
    unique_multiples = set()
    
    # Find unique multiples for each number in the list
    for m in unique_multiples_list:
        # Start from the first multiple of m that is <= limit
        current_multiple = m
        while current_multiple <= limit:
            # Only add if this multiple is not already in the set
            if current_multiple not in unique_multiples:
                unique_multiples.add(current_multiple)
            current_multiple += m
    
    # Return the sum of unique multiples
    return sum(unique_multiples)