def reverse_words(input_string):
    """
    Reverses the order of words in a given string while preserving word characters.
    
    Args:
        input_string (str): The input string to reverse word order.
    
    Returns:
        str: A string with words in reversed order, preserving original word characters.
    
    Examples:
        >>> reverse_words("Hello World")
        'World Hello'
        >>> reverse_words("  Hello   World  ")
        'World Hello'
        >>> reverse_words("Hello123 World456")
        'World456 Hello123'
        >>> reverse_words("")
        ''
    """
    # Handle empty string case
    if not input_string:
        return ""
    
    # Split the string by whitespace, removing extra spaces
    words = input_string.split()
    
    # Reverse the order of words
    reversed_words = words[::-1]
    
    # Join the reversed words with a single space
    return " ".join(reversed_words)