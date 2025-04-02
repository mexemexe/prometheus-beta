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
    current_substring = ""
    
    # Use a dictionary to track character positions
    char_positions = {}
    
    for i, char in enumerate(s):
        # If character is already in current substring, reset substring
        if char in char_positions:
            # Check if current substring is longer than previous longest
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            
            # Reset current substring to start after the previous occurrence
            prev_index = char_positions[char]
            current_substring = s[prev_index + 1:i + 1]
        else:
            # Extend current substring
            current_substring += char
        
        # Update character position
        char_positions[char] = i
    
    # Final check after loop
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring
    
    return longest_substring