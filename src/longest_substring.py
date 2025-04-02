def find_longest_substring(s: str) -> str:
    """
    Find the longest substring without repeating characters.
    
    Args:
        s (str): Input string to search for the longest unique substring
    
    Returns:
        str: The longest substring without repeating characters
             If multiple such substrings exist, return the first one
             If the input is empty, return an empty string
    
    Time Complexity: O(n)
    Space Complexity: O(min(m, n)), where m is the size of the character set
    """
    # Handle empty string case
    if not s:
        return ""
    
    # Initialize variables to track the longest substring
    start = 0
    longest_start = 0
    longest_length = 0
    char_positions = {}
    
    for end, char in enumerate(s):
        # If character is already seen and its last position is after or at the start index
        if char in char_positions and char_positions[char] >= start:
            # Update start to next position after previous occurrence
            start = char_positions[char] + 1
        else:
            # Check if current substring is longer than the longest found
            current_length = end - start + 1
            if current_length > longest_length:
                longest_start = start
                longest_length = current_length
        
        # Update the last seen position of the character
        char_positions[char] = end
    
    return s[longest_start:longest_start + longest_length]