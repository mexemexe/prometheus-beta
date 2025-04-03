def capitalize_comma_words(input_string: str) -> str:
    """
    Capitalize words in a comma-separated string of alphabetical characters.

    Args:
        input_string (str): A string of words separated by commas, 
                             containing only alphabetical characters.

    Returns:
        str: A new string with each word capitalized.

    Raises:
        ValueError: If input contains non-alphabetical characters or whitespace.
    """
    # Validate input
    if not input_string.replace(',', '').isalpha():
        raise ValueError("Input must contain only alphabetical characters and commas")

    # Split the string, capitalize each word, and rejoin
    words = input_string.split(',')
    capitalized_words = [word.capitalize() for word in words]
    return ','.join(capitalized_words)