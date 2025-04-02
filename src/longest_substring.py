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
    longest_substring = ""
    start = 0
    char_positions = {}
    
    for end, char in enumerate(s):
        # If character is already seen and its last position is after or at the start index
        if char in char_positions and char_positions[char] >= start:
            # Move the start to the next position after the last occurrence
            start = char_positions[char] + 1
        else:
            # Update longest substring if current substring is longer
            current_substring = s[start:end+1]
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
        
        # Update the last seen position of the character
        char_positions[char] = end
    
    return longest_substring