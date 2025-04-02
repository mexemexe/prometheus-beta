def is_balanced_parentheses(s: str) -> bool:
    """
    Check if a string of parentheses is balanced.
    
    A string of parentheses is considered balanced if:
    - Every opening parenthesis has a corresponding closing parenthesis
    - Parentheses are closed in the correct order
    
    Args:
        s (str): A string containing only parentheses characters '(' and ')'
    
    Returns:
        bool: True if parentheses are balanced, False otherwise
    
    Examples:
        >>> is_balanced_parentheses("()")
        True
        >>> is_balanced_parentheses("((()))")
        True
        >>> is_balanced_parentheses("(())")
        True
        >>> is_balanced_parentheses(")(")
        False
        >>> is_balanced_parentheses("(()")
        False
        >>> is_balanced_parentheses("")
        True
    """
    # Handle empty string case
    if not s:
        return True
    
    # Stack to keep track of opening parentheses
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        if char == '(':
            # Push opening parenthesis onto the stack
            stack.append(char)
        elif char == ')':
            # If closing parenthesis and no opening parenthesis, it's unbalanced
            if not stack:
                return False
            
            # Remove the most recent opening parenthesis
            stack.pop()
    
    # If stack is empty, all parentheses are balanced
    return len(stack) == 0