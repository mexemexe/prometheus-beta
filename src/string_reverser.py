def reverse_string_in_place(s: list) -> None:
    """
    Reverse a string in-place with O(1) space complexity.
    
    This function modifies the input list of characters directly,
    swapping characters from the start and end until the middle is reached.
    
    Args:
        s (list): A list of characters to be reversed in-place.
    
    Time Complexity: O(n), where n is the length of the string
    Space Complexity: O(1), as no additional list is created
    
    Raises:
        TypeError: If input is not a list
    
    Examples:
        >>> chars = list('hello')
        >>> reverse_string_in_place(chars)
        >>> chars
        ['o', 'l', 'l', 'e', 'h']
    """
    # Validate input is a list
    if not isinstance(s, list):
        raise TypeError("Input must be a list of characters")
    
    # Handle empty list or single-character list
    if len(s) <= 1:
        return
    
    # Two-pointer approach to swap characters
    left, right = 0, len(s) - 1
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        
        # Move pointers towards center
        left += 1
        right -= 1