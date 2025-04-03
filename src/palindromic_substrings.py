def find_palindromic_substrings(s):
    """
    Find all palindromic substrings in a given string.
    
    A palindromic substring is a sequence of characters that reads the same 
    forwards and backwards.
    
    Args:
        s (str): The input string to search for palindromic substrings
    
    Returns:
        list: A list of all palindromic substrings found in the input string
    
    Examples:
        >>> find_palindromic_substrings("abba")
        ['a', 'b', 'bb', 'abba']
        >>> find_palindromic_substrings("abc")
        ['a', 'b', 'c']
    """
    # Handle edge cases
    if not s or not isinstance(s, str):
        return []
    
    # Set to store unique palindromic substrings
    palindromes = set()
    
    # Check all possible substrings
    for i in range(len(s)):
        # Odd length palindromes
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1
        
        # Even length palindromes
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1
    
    # Convert to sorted list for consistent output
    return sorted(list(palindromes), key=len)